# Documentation Index

This directory is the canonical documentation root for K2 Daily Brief.

## Authority Order

### Product Behavior
1. `docs/product/REQUIREMENTS.md`
2. `docs/architecture/ARCHITECTURE.md`
3. `docs/architecture/ROUTES_V1.md`
4. `docs/architecture/UI_V1.md`
5. `docs/architecture/DATA_MODEL.md`
6. `docs/product/PRODUCT_PHASES.md`
7. `docs/architecture/JOB_EXECUTION_SEMANTICS.md`

### Agent Workflow
1. `AGENTS.md`
2. `docs/harness/commands.md`
3. `docs/harness/task-handshake.md`
4. `docs/harness/testing-policy.md`
5. `docs/harness/commit-policy.md`
6. `docs/harness/maintenance.md`
7. `docs/workflow/TODO.md`
8. `docs/workflow/PROGRESS.md`

## Structure
- `docs/product/` product scope and requirements
- `docs/architecture/` technical architecture and data semantics
- `docs/harness/` agent operating policies
- `docs/workflow/` task queue and progress log
- `docs/decisions/` ADRs and major decision records
- `docs/interview/` reusable multi-pass interview kit for gathering new-project documentation inputs

## Validation
Run:

```bash
./scripts/validate_docs.sh
```
