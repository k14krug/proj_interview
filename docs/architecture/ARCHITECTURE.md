# ARCHITECTURE.md
Project: K2 Daily Brief

---

## 1. System Overview

K2 Daily Brief is a locally hosted, multi-user news aggregation and AI synthesis system.

Phase 1 (V1) represents the editorial engine foundation. Reader abstraction and automation are intentionally excluded (see `docs/product/PRODUCT_PHASES.md`).

---

## 2. Environments

### Development
- WSL Ubuntu
- MySQL 8.x
- VS Code
- Flask dev server
- .env configuration

### Production
- Linux (ThinkPad W550)
- MySQL 8.x at 127.0.0.1:3306
- Gunicorn + systemd
- Nginx reverse proxy
- Cloudflare Tunnel

Environments must behave identically at the application layer.

---

## 3. Core Stack

- Flask (App Factory required)
- Jinja2 server-rendered templates
- HTMX (partial updates + polling UX)
- Bootstrap 5 (UI layout/components baseline)
- SQLAlchemy
- Alembic
- MySQL 8.x only
- OpenAI API
- APScheduler (background scheduler)
- pytest
- python-dotenv

---

## 4. Architectural Principles

1. Strict separation of concerns
2. No business logic in routes
3. No AI calls inside routes
4. Immutable generated content (articles + briefings)
5. Multi-user isolation enforced
6. UTC storage, local-time rendering
7. No automation creep in V1
8. Event Clusters are internal structural objects
9. Source-only guarantees must be enforced via validation (not just “prompt wording”)

---

## 5. Background Processing (Single-Execution Safe)

### V1 (Required for Production Safety)

**Background jobs MUST run in a single dedicated process**, not inside Gunicorn workers.

Rationale: running APScheduler inside the Flask app while deployed with Gunicorn can create one scheduler per worker, duplicating jobs.

Implementation:
- systemd service: `k2dailybrief-worker`
- Runs APScheduler and calls the same `services/` functions used by the web app.
- Controlled by `.env` (e.g., `WORKER_ENABLED=true` for worker, false for web).

Jobs:
- RSS ingestion
- Event Cluster updates
- Cleanup (retention-managed tables only; see deletion policy)

Execution contract (V1):
- Operational guarantee is **at-most-once per schedule slot** (not exactly-once under all failure modes).
- Job handlers must be idempotent so reruns are safe after crashes/restarts.
- Scheduler should set `max_instances=1` per job to prevent in-process overlap.
- Scheduler should define explicit `coalesce` and `misfire_grace_time` per job.

Job-run ledger:
- Persist runs in `job_runs` with unique (`job_name`, `scheduled_for`).
- Before execution, insert/check the slot; if already claimed, skip.
- If a prior run remains `running` beyond timeout threshold, mark `skipped_timeout` and continue according to policy.
- On worker startup, run recovery for stale `running` rows from the same `worker_instance` and mark them `failed` before normal scheduling resumes.

### Development

Two supported modes:
- Simple: run worker + web separately (recommended once stable)
- Fast iteration: allow in-process scheduler only when explicitly enabled and web runs single-process

---

## 6. Database Layer

- MySQL 8.x only
- Host: 127.0.0.1:3306
- utf8mb4 charset
- utf8mb4_0900_ai_ci collation

All timestamps stored in UTC.
No reliance on MySQL timezone functions.

### 6.1 Migration Baseline Commands

Migration tooling is standardized on Alembic using `alembic.ini` at repository root.

- Apply latest schema:
  - `python3 -m alembic upgrade head`
- Create a new migration:
  - `python3 -m alembic revision -m "describe_change"`
- Roll back one migration:
  - `python3 -m alembic downgrade -1`

Connection resolution order:
1. `K2_DATABASE_URL` (explicit override for tests/local tooling)
2. `.env` / config (`K2_DB_HOST`, `K2_DB_PORT`, `K2_DB_NAME`, `K2_DB_USER`, `K2_DB_PASSWORD`) using MySQL 8 + `mysql+pymysql`.

---

## 7. Data Flow

1. RSS ingestion → raw_articles (+ optional full text)
2. Similarity logic → Event Clusters
3. Cluster depth scoring computes Information Gap indicator (`Thin`/`Moderate`/`High Depth`)
4. User-specific filtering layer applies source preferences to cluster and source-article visibility
5. User selects source articles
6. Generate request creates async job (`queued` → `running`)
7. AI generates Article (with inline citations + “Sources Used”)
8. Validator confirms citations map to selected sources
9. Citation provenance map is persisted for Synthesis Audit (V1: source-linked, excerpt when available)
10. Article stored immutable (`success`) or marked `failed`
11. User compiles Daily Brief snapshot (immutable)

---

## 8. AI Integration

Located in: `app/services/ai_service.py`

Responsibilities:
- Build prompts with strict source list and citation requirements
- Call OpenAI API
- Store prompt + response + metadata
- Apply accuracy-over-length policy and low-information generation mode when source depth is limited
- Validate citation mapping
- Persist citation provenance records for audit UI
- Mark failures and optionally retry

Validation (V1 acceptance rule):
- Article must include “Sources Used” list of selected URLs
- Inline citations must reference only those URLs
- If invalid, reject/regenerate or mark failed

AI must not:
- Fetch URLs
- Modify existing articles or briefings
- Rewrite stored content

---

## 9. UI Philosophy

V1 UI is structured and controlled. It may expose workflow elements but shall not label itself as “Newsroom Mode.”
V1 implementation is server-rendered first: Jinja2 templates + HTMX interactions + Bootstrap 5 base components.
Client-side JavaScript should remain minimal and page-scoped in V1.
Generation UX should display explicit async states (`queued`, `running`, `success`, `failed`) and poll for completion instead of waiting on a long HTTP response.
Cluster list/detail UX should show Information Gap indicators.
Generated article UX should include a Synthesis Audit panel (citation → source URL, with excerpt evidence when available).
Canonical route semantics are defined in `docs/architecture/ROUTES_V1.md`.
Canonical layout and route-level UI interaction contracts are defined in `docs/architecture/UI_V1.md`.

Final product will abstract operational mechanics into a clean Daily Reader experience.

---

## 10. Testing

pytest required for:
- Models
- Clustering logic
- User isolation
- Prompt construction + citation validation
- Brief compilation
- Ingestion idempotency (dedupe + repeat runs)
- Immutability enforcement (no update/delete on immutable tables)
- Worker single-execution safety (no duplicate job runs per schedule)
- Misfire/restart handling (slot claim behavior via `job_runs`)
- Startup recovery behavior for stale `running` rows by `worker_instance`
- Overlap prevention (`max_instances=1` behavior)
- Cluster visibility filtering by per-user source preferences
- Information Gap indicator computation and labeling behavior
- Async generation status transitions and polling behavior
- Citation provenance persistence and Synthesis Audit rendering (V1-lite)

AI calls must be mocked.

---

## 11. Deployment

### Web
- Gunicorn + systemd (`k2dailybrief-web`)
- Nginx reverse proxy
- Cloudflare Tunnel
- MySQL local only

### Worker
- APScheduler + systemd (`k2dailybrief-worker`)
- Uses same codebase + .env
- Exactly one instance in production

Development:
- Flask dev server + separate worker (recommended)
- Same DB engine
- Same .env model

App Factory ensures parity.
