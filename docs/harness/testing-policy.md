# Testing Policy

## Baseline Rule
Every task that changes behavior should include tests when the behavior is testable.

Canonical local command:
- `./scripts/run_tests.sh`
- Equivalent direct command: `python3 -m pytest`

## Route Coverage Rule
- If a task has `Route Links` with one or more `RT-*` IDs, add or update integration tests that exercise those route semantics.
- Route IDs are defined in `docs/architecture/ROUTES_V1.md`.
- UI state behavior for those routes is defined in `docs/architecture/UI_V1.md` and should be covered where testable.

## Minimum Expectations
- Unit/service tests for business logic.
- Integration tests for workflow-critical paths.
- AI calls mocked in tests (use injected fake clients/fixtures, never live API calls).

## When Tests Are Not Added
If behavior changed and no tests were added:
1. Explain why in `docs/workflow/PROGRESS.md`.
2. Add explicit follow-up test task in `docs/workflow/TODO.md`.

## Test Reporting
For each task entry in `docs/workflow/PROGRESS.md`, record:
- test command(s) used
- result summary
- known test gaps
