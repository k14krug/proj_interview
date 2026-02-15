# Documentation Index (Template)

This `docs/` tree is a reusable **template** for starting new projects with an AI agent.

Start a new project by running the interview process in `docs/interview/` and drafting a full docs set in `docs/_draft_<project>/`. After freeze, replace the canonical docs under `docs/` with the finalized draft.

Concrete examples live in `docs/examples/`.

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
- `docs/product/` product scope and requirements (template)
- `docs/architecture/` technical architecture and data semantics (template)
- `docs/harness/` agent operating policies (generally reusable)
- `docs/workflow/` task queue and progress log templates
- `docs/decisions/` ADRs and major decision records
- `docs/interview/` multi-pass interview kit for gathering new-project documentation inputs
- `docs/examples/` frozen example documentation sets (non-authoritative)

## Validation
Run:

```bash
./scripts/validate_docs.sh
```

