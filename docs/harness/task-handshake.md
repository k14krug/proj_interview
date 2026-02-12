# Task Handshake Protocol

A task is complete only when all items below are satisfied.

## Completion Checklist
1. Scoped code/docs changes are complete.
2. Acceptance criteria in `docs/workflow/TODO.md` are satisfied.
3. `Requirement Links` in the task are addressed by implementation and/or explicit blocker notes.
4. For route-affecting tasks, `Route Links` map to `RT-*` IDs in `docs/architecture/ROUTES_V1.md` and behavior aligns with `docs/architecture/UI_V1.md`.
5. Tests are added/updated when the task is testable.
6. Route-linked tasks include integration tests for linked route semantics.
7. Relevant tests are run, or a reason for not running tests is documented.
8. For successful task execution, a local scoped commit is created using `type(PH-XX-YY): ...` format before marking the task `[x]`.
9. Task status in `docs/workflow/TODO.md` is updated (`[/]` -> `[x]` or `[!]`).
10. A transaction entry is appended to `docs/workflow/PROGRESS.md`.

## Required PROGRESS Entry Fields
- Timestamp (UTC)
- Task ID
- Type
- Status
- Accomplished
- Files Changed
- Commit Header(s): required for successful `PH-XX-YY` task entries; use `N/A` only when no commit is required (for example, non-task work).
- Tests Added/Updated
- Test Results
- Technical Debt / Known Gaps
- Next Step
- Blockers (if any)

## Blocked Task Behavior
If blocked:
1. Mark task `[!]`.
2. Record blocker detail and concrete unblock condition.
3. Propose the next actionable step in `docs/workflow/PROGRESS.md`.
