# Command Switches

This file defines behavior for slash-style command switches.

## Global Safeties

1. Do not modify `AGENTS.md` without explicit user approval. If a change seems necessary, stop and ask for approval first.

## ID Conventions
- Task ID format: `PH-XX-YY`
  - `XX` = execution phase number (2 digits)
  - `YY` = task number within phase (2 digits)
- Ad hoc ID format: `AH-XX`

Terminology:
- Product Phase (V1/V2) comes from `docs/product/PRODUCT_PHASES.md`.
- Execution Phase sections in `docs/workflow/TODO.md` are batching constructs for task execution.
- `PH-XX-YY` binds to Execution Phase sections only.

## `/TASK [PH-XX-YY]`
Execute one task from `docs/workflow/TODO.md`.

Preconditions:
1. `docs/workflow/TODO.md` exists.
2. Requested ID exists and matches `PH-XX-YY`.
3. Task status is `[ ]` or `[/]`.
4. Task includes `Requirement Links`, `Route Links`, scope, acceptance criteria, and memory-bank context.

Execution:
1. Read task context first.
2. Mark task `[/]` when work starts.
3. Implement only scoped changes.
4. Add/update tests when behavior changes and is testable.
5. If `Route Links` contains `RT-*`, implement semantics from `docs/architecture/ROUTES_V1.md` and UI behavior from `docs/architecture/UI_V1.md`, then add/update integration tests.
6. Run relevant tests or record why tests were not run.
7. Create one local scoped commit for the task's completed work using header format from `docs/harness/commit-policy.md` (for example: `feat(PH-XX-YY): ...`). This commit is required before marking the task `[x]`.
8. Update `docs/workflow/TODO.md` and append log entry in `docs/workflow/PROGRESS.md`.
9. Mark task `[x]` on success or `[!]` on blocker.

If any precondition fails, stop and report the issue.

## `/PHASE [XX]`
Execute all eligible tasks in one execution phase from `docs/workflow/TODO.md`.

Interpretation:
1. `XX` is a two-digit execution phase number.
2. Target section is `## Execution Phase XX`.
3. Eligible tasks are `PH-XX-YY` in that section with status `[ ]` or `[/]`.

Preconditions:
1. `docs/workflow/TODO.md` exists.
2. Requested execution phase section exists and matches `Execution Phase XX`.
3. At least one eligible `PH-XX-YY` task exists in the target section.
4. Each eligible task includes `Requirement Links`, `Route Links`, scope, acceptance criteria, and memory-bank context.

Execution:
1. Read full phase section context first.
2. Execute tasks in ascending task ID order (`PH-XX-01`, `PH-XX-02`, ...).
3. For each task, follow `/TASK` rules exactly (status transitions, route/UI semantics, tests, local commit requirement, and progress logging).
4. After each task:
   - Continue on success.
   - Confirm a local commit was created for each task marked `[x]` before moving to the next task.
   - Stop phase execution on `[!]` blocked status and report blocker with concrete unblock condition.
5. On completion, provide a phase summary:
   - tasks completed
   - tasks blocked
   - tests run / not run
   - next actionable task ID

Resume behavior:
1. Re-running `/PHASE [XX]` skips `[x]` tasks automatically.
2. Re-running starts from the first remaining `[ ]` or `[/]` task.

If any precondition fails, stop and report the issue.

## `/ADHOC [Description]`
Perform one-off tooling/environment operations.

Rules:
1. Description must be non-empty.
2. Generate next ad hoc ID as `AH-XX` by incrementing highest existing `AH-*` in `docs/workflow/PROGRESS.md`.
3. Keep scope limited to the request.
4. Record full action in `docs/workflow/PROGRESS.md`.

If ID generation fails or description is missing, stop and report the issue.

## `/PLAN`
Planning mode without code implementation.

Rules:
1. Review product authority docs and `docs/workflow/TODO.md`.
2. Confirm execution phase sections and ID formats are valid.
3. Propose top 3 next tasks using `PH-XX-YY`.
4. Include dependencies, risks, and testing expectations.

If required inputs are missing, stop and report the issue.

## `/INTERVIEW [ProjectName]`
Run the documentation interview process to produce a new project docs set before any implementation work.

Preconditions:
1. `docs/interview/` exists.
2. `ProjectName` is provided (used for naming interview artifacts and draft tree).
3. You have explicit user approval before modifying `AGENTS.md`.

Execution:
1. Create interview artifacts (do not edit templates in place):
   - Copy `docs/interview/INTERVIEW_SESSION_TEMPLATE.md` to `docs/interview/<ProjectName>_INTERVIEW_SESSION.md`.
   - Copy `docs/interview/ANSWER_LEDGER_TEMPLATE.md` to `docs/interview/<ProjectName>_ANSWER_LEDGER.md`.
2. Create a parallel draft tree at `docs/_draft_<ProjectName>/` mirroring the final structure (`product/`, `architecture/`, `harness/`, `workflow/`).
3. Requirements intake (before asking Set 01):
   - Ask whether a requirements doc already exists.
   - If it exists, request its location and format (Markdown or plain text).
   - Use it as a seed: extract what it already answers, record those items in the ledger with source references, and draft `docs/_draft_<ProjectName>/product/REQUIREMENTS.md` from it.
4. Draft continuously during the interview:
   - As each set reaches `decided` on its critical items, update the corresponding files under `docs/_draft_<ProjectName>/`.
   - Do not wait until all sets are complete to start drafting.
5. Conduct the interview using:
   - process rules in `docs/interview/INTERVIEW_PROCESS.md`
   - question sets in `docs/interview/QUESTION_SETS.md`
   - answer-to-doc mapping in `docs/interview/DOCUMENT_MAPPING.md`
6. Ask only what is missing, ambiguous, or contradictory:
   - If the existing requirements doc already answers a baseline question, skip it.
   - If the doc is ambiguous or contradictory, ask brief confirmation questions to resolve it.
7. Scrub old product names/assumptions from all drafted docs per `docs/interview/SCRUB_CHECKLIST.md`.
8. Freeze only when criteria in `docs/interview/INTERVIEW_PROCESS.md` are satisfied.
9. After freeze, replace canonical docs under `docs/` with the finalized draft from `docs/_draft_<ProjectName>/`.
10. Only after docs are frozen, proceed to implementation work using `/TASK` and `/PHASE`.

Stop conditions:
1. If asked to change application code before freeze, stop and confirm the user wants to shift from interview (docs) to implementation (code).
2. If a change to `AGENTS.md` is needed, stop and ask for explicit approval before proceeding.
