# K2 Daily Brief — AGENTS.md

Version: 2.1
Last Updated: 2026-02-12
Change Summary: Added `/PHASE [XX]` slash command entry point for iterating all tasks in an execution phase.

---

## 1. Purpose
This file is the entry map for agent operation. Detailed policy lives in `docs/harness/`.

---

## 2. Canonical Doc Map

### Product Authority (highest to lowest)
1. `docs/product/REQUIREMENTS.md`
2. `docs/architecture/ARCHITECTURE.md`
3. `docs/architecture/ROUTES_V1.md`
4. `docs/architecture/UI_V1.md`
5. `docs/architecture/DATA_MODEL.md`
6. `docs/product/PRODUCT_PHASES.md`
7. `docs/architecture/JOB_EXECUTION_SEMANTICS.md`

### Execution Harness
1. `AGENTS.md` (entry map)
2. `docs/harness/commands.md`
3. `docs/harness/task-handshake.md`
4. `docs/harness/testing-policy.md`
5. `docs/harness/commit-policy.md`
6. `docs/harness/maintenance.md`
7. `docs/workflow/TODO.md`
8. `docs/workflow/PROGRESS.md`

If docs conflict, the higher item in Product Authority wins unless explicitly overridden by the user.

---

## 3. Slash Command Entry Points
- `/TASK [PH-XX-YY]` -> `docs/harness/commands.md`
- `/PHASE [XX]` -> `docs/harness/commands.md`
- `/ADHOC [Description]` -> `docs/harness/commands.md`
- `/PLAN` -> `docs/harness/commands.md`

Task and ad hoc IDs:
- Task: `PH-XX-YY` (execution phase tracking ID)
- Ad hoc: `AH-XX`

Terminology:
- Product Phase: V1/V2 product scope defined in `docs/product/PRODUCT_PHASES.md`.
- Execution Phase: planning/work batching sections in `docs/workflow/TODO.md`.
- `PH-XX-YY` references Execution Phase IDs only, not Product Phase readiness.

---

## 4. Always-Enforced Invariants
- Multi-user isolation by `user_id` on user-facing paths.
- UTC timestamps in storage.
- V1 scope discipline (no Phase 2 implementation in V1 paths).
- Background-job safety rules from `docs/architecture/JOB_EXECUTION_SEMANTICS.md`.

---

## 5. Validation
Run harness validation before and after substantial doc/workflow changes:

```bash
./scripts/validate_docs.sh
```

If validation fails, stop and report issues before proceeding.
