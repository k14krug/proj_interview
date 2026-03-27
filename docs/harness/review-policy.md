# Review Policy

This file defines when reviewer involvement is required and what the reviewer is allowed to do.

## Purpose
The reviewer is a separate role from the implementer.

The reviewer checks whether completed task work actually satisfies:
- task scope
- acceptance criteria
- requirement and route links
- testing expectations
- commit and progress-log discipline

The reviewer is not the primary implementer unless explicitly instructed by the user.

## Reviewer Inputs
For a task review, the reviewer must inspect:
1. The target task in `docs/workflow/TODO.md`
2. Linked authority docs referenced by the task (`REQUIREMENTS.md`, `ROUTES_V1.md`, `UI_V1.md`, `DATA_MODEL.md`, `JOB_EXECUTION_SEMANTICS.md`, etc. as applicable)
3. Changed files for the task
4. Tests added/updated for the task
5. Test results recorded or produced during task execution
6. Relevant `docs/workflow/PROGRESS.md` entry content for the task

## Reviewer Output
Reviewer output must end with exactly one disposition:
- `PASS`
- `PASS WITH GAPS`
- `FAIL`

Reviewer findings must be grouped as:
- `Blocker` = must be fixed before the task is considered complete
- `Should-Fix` = important but non-blocking follow-up
- `Note` = observation only

## Mandatory Review Triggers
A task requires reviewer involvement if any of the following are true:
1. The task includes one or more `Route Links` (`RT-*`).
2. The task changes authentication, authorization, ownership, privacy, or multi-user isolation behavior.
3. The task changes schema, migrations, persistence contracts, indexing contracts, or data model semantics.
4. The task changes background jobs, retry behavior, scheduling, worker semantics, or concurrency-sensitive flows.
5. The task changes file upload, file serving, artifact storage, or external API/provider integration.
6. The task changes AI call routing, retrieval gating, logging, cost accounting, or other trust-sensitive AI behavior.
7. Tests were not added for a behavior-changing task, or relevant tests were not run.
8. The task required manual verification for a behavior-critical path.
9. The task has explicit high-risk notes in `docs/workflow/TODO.md`.
10. The user explicitly requests review.

## Optional Review Triggers
Reviewer involvement is recommended but not mandatory for:
- medium-scope refactors
- UI behavior changes without route or contract changes
- non-trivial template/JS changes
- config work that does not affect security or runtime contracts

## Tasks That Usually Do Not Need Review
Reviewer involvement is usually not required for:
- wording/copy-only changes
- comment-only changes
- formatting-only changes
- doc-only updates not tied to a `PH-XX-YY` implementation task
- very small cosmetic CSS adjustments with no behavior change

If there is uncertainty, treat the task as review-required.

## Reviewer Responsibilities
The reviewer must check:
1. The implementation stayed within task scope.
2. Acceptance criteria are actually satisfied.
3. `Requirement Links` are addressed.
4. For route-linked tasks, linked `RT-*` semantics align with `docs/architecture/ROUTES_V1.md` and `docs/architecture/UI_V1.md`.
5. Tests meet `docs/harness/testing-policy.md`.
6. Any missing tests or skipped tests are explicitly justified and followed by a concrete follow-up task when required.
7. The task satisfies `docs/harness/task-handshake.md`.
8. A scoped commit exists for successful `PH-XX-YY` completion per `docs/harness/commit-policy.md`.
9. `docs/workflow/PROGRESS.md` reflects meaningful completion details and known gaps.

## Reviewer Limits
The reviewer must not:
- silently expand task scope
- silently rewrite large portions of implementation
- waive missing acceptance criteria
- waive missing required tests without explicit justification
- modify `AGENTS.md` without explicit user approval
- mark a task complete if blocker findings remain

The reviewer may propose concrete fixes, but implementation remains a separate step unless the user explicitly asks the reviewer to apply fixes.

## Execution Timing
For review-required tasks:
1. Implement the task.
2. Add/update tests.
3. Run relevant tests or record why tests were not run.
4. Run reviewer pass before final completion.
5. Resolve blocker findings.
6. Create the required local scoped commit.
7. Update `docs/workflow/TODO.md` and `docs/workflow/PROGRESS.md`.
8. Mark the task complete only after reviewer disposition is `PASS` or `PASS WITH GAPS`.

## Phase-Level Review
`/PHASE` execution also includes a phase-end review summary.

Phase-end review is for:
- cross-task drift
- dependency mistakes
- recurring technical debt
- missed follow-up tasks
- inconsistent assumptions across tasks in the phase

Phase-end review does not replace mandatory task-level review for review-required tasks.