# JOB_EXECUTION_SEMANTICS.md
Project: K2 Daily Brief

## 1. Purpose

This document defines how background jobs execute in Phase 1 (V1) to ensure:

- No duplicate scheduled executions  
- Safe behavior on crash or restart  
- Idempotent ingestion  
- Clear operational boundaries  

V1 uses a **single dedicated worker process**.

---

## 2. Production Execution Model

Production consists of two independent services:

- `k2dailybrief-web` (Gunicorn)
- `k2dailybrief-worker` (APScheduler)

Only the worker runs scheduled jobs.

The web process must never run APScheduler.

---

## 3. Execution Guarantees (V1)

V1 guarantees:

- Exactly one active worker process.
- At-most-one execution claim per (`job_name`, `scheduled_for`) schedule slot.
- No concurrent execution of the same job instance.
- Safe restart after crash.
- Idempotent ingestion and clustering.

V1 does NOT guarantee:

- Distributed locking
- Cross-host coordination
- Multi-node scaling

---

## 4. Core Jobs (V1)

1. RSS Ingestion
2. Event Clustering
3. Retention Cleanup (restricted tables only)

Each job must follow the rules below.

---

## 5. Job Run Tracking Table

### job_runs

| Field | Type | Notes |
|-------|------|-------|
| id | PK |
| job_name | VARCHAR(128) | e.g., rss_ingestion |
| scheduled_for | DATETIME (UTC) | Canonical schedule slot timestamp |
| started_at | DATETIME (UTC) |
| finished_at | DATETIME (UTC) nullable |
| status | ENUM('running','success','failed','skipped_timeout') |
| worker_instance | VARCHAR(128) nullable | process/host identifier |
| error_message | TEXT nullable |

Indexes/constraints:
- Unique: (`job_name`, `scheduled_for`)
- Index: status
- Index: started_at

Purpose:
Track execution lifecycle and enforce slot-level execution claims.

---

## 6. Single-Execution Rule

Before executing a job:

1. Compute the canonical `scheduled_for` slot timestamp (UTC) for the trigger.
2. Optionally check stale `running` rows for the same `job_name`:
   - If `started_at < (now - MAX_RUNTIME_THRESHOLD)`, mark stale row as `skipped_timeout` with `finished_at=now`.
3. Attempt an atomic slot-claim insert:
   - `INSERT INTO job_runs(job_name, scheduled_for, started_at, status, worker_instance) VALUES (..., ..., now, 'running', ...)`

4. If insert fails due to unique (`job_name`, `scheduled_for`):
   - Skip execution (slot already claimed/executed).
5. Execute job.

6. On success:
   - Update status = 'success'
   - Set finished_at

7. On failure:
   - Update status = 'failed'
   - Set error_message
   - Set finished_at

This avoids check-then-insert races and enforces at-most-once per schedule slot.

---

## 7. Crash / Restart Semantics

If worker crashes mid-job:

- status remains 'running'
- On next scheduled run:
  - If started_at older than threshold → mark stale run as `skipped_timeout`, then continue with slot claim logic.

Threshold recommendation:
- 2x expected max runtime

Example:
If ingestion expected max runtime is 5 minutes,
set threshold = 10 minutes.

---

## 7.1 Startup Recovery Routine (Worker Boot)

On worker start, before scheduling loop begins:

1. Identify stale rows in `job_runs` where:
   - `status = 'running'`
   - `worker_instance` matches the prior instance identity (or unknown instance policy)
2. Mark them `failed` with:
   - `finished_at = now`
   - `error_message = 'worker_startup_recovery'` (or equivalent reason)
3. Emit recovery logs/metrics.

Purpose:
- Avoid waiting for next schedule tick to reconcile abandoned `running` rows.
- Restore operational visibility immediately after crash/reboot.

---

## 8. Idempotency Boundaries

### 8.1 RSS Ingestion

Idempotent by design:

- raw_articles.url is UNIQUE
- Duplicate inserts fail cleanly
- Ingestion loop must catch and ignore duplicate errors

Safe to re-run.

---

### 8.2 Event Clustering

Clustering must be idempotent:

- cluster_articles has UNIQUE(cluster_id, raw_article_id)
- Re-evaluating assignment must not duplicate links
- article_count must only increment on successful insert

Safe to re-run.

---

### 8.3 Retention Cleanup

Cleanup must:

- Only target purge-allowed tables
- Never delete rows referenced by immutable tables
- Run inside a transaction
- Log deleted counts

Cleanup must be safe to re-run without side effects.

---

## 9. APScheduler Configuration (V1)

Required:
- `max_instances = 1` per job (prevents overlap in a process)
- `coalesce` explicitly set per job
- `misfire_grace_time` explicitly set per job

Recommended defaults (tune by job):
- `coalesce = True` for ingestion/clustering
- `misfire_grace_time = 300` seconds for frequent jobs (or larger for heavy jobs)

Scheduler settings complement (but do not replace) DB slot claims.

---

## 10. Manual Trigger Semantics

If jobs can be manually triggered:

- Manual run must respect same single-execution rule.
- Manual run must claim a `job_runs` slot using explicit `scheduled_for`.
- No bypassing concurrency checks.

---

## 11. Observability

Worker must log:

- Job start
- Job end
- Duration
- Rows processed
- Errors

job_runs table serves as structured audit log.

---

## 12. At-Most-Once Definition (V1 Context)

“At-most-once per schedule slot” in V1 means:

- At most one successful claim per (`job_name`, `scheduled_for`) slot.
- No overlapping concurrent runs.
- Safe restart behavior.
- No duplicate data side effects due to idempotency constraints.

It does not mean:

- Distributed consensus-level exactly-once delivery.
- Transactional event-stream guarantees.

V1 aims for operational correctness, not distributed-system guarantees.

---

## 13. Future Evolution (Not V1)

If system scales beyond one host:

- Replace local lock logic with DB-based advisory locks or Redis locks.
- Consider leader-election model.
- Possibly separate ingestion and clustering workers.

Not required in V1.
