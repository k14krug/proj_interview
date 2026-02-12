# Commit Policy

This repo currently uses a local, no-branch-default workflow.

## Branching
- Do not create branches unless explicitly requested.

## Commit Trigger
- `/TASK` and `/PHASE` execution: create one local commit for any work associated with each successfully completed `PH-XX-YY` task.
- Non-task work outside `/TASK` or `/PHASE`: commit only when explicitly requested by the user.

## Commit Header Format
- Task work: `type(PH-XX-YY): short summary`
- Ad hoc work: `type(AH-XX): short summary`

Example:
- `feat(PH-01-01): define information gap scoring formula`

## Commit Quality
- Keep commits atomic.
- Include only scoped changes.
- For successful task execution, `Commit Header(s)` in `docs/workflow/PROGRESS.md` must contain the created commit header (not `N/A`).
- A `PH-XX-YY` task is not considered complete until its local commit exists.
- If no commit was requested for non-task work, record `N/A` in `Commit Header(s)` in `docs/workflow/PROGRESS.md`.
