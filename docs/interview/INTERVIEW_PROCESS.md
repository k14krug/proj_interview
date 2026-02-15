# Interview Process

This process is for producing a clean, implementation-ready **documentation set** for a new project. It is not a coding workflow.

Hard requirements:
1. **`AGENTS.md` may only be changed after explicit user approval.** Default behavior is to treat it as fixed and only verify that it still matches the new project's governance needs.
2. Use a **parallel draft tree** (recommended): draft new docs under `docs/_draft_<project>/` and only replace canonical docs under `docs/` after freeze.
3. Before freeze, perform a **scrub pass** to remove old product names/assumptions from all drafted documents (see `docs/interview/SCRUB_CHECKLIST.md`).

## 1. Operating Model

Use a four-pass loop. Do not try to finalize everything in one pass.

1. Pass 1: Baseline discovery.
2. Pass 2: Constraint and edge-case probing.
3. Pass 3: Conflict resolution and tradeoff decisions.
4. Pass 4: Freeze, acceptance checks, and doc drafting handoff.

## 2. Question Cycle (Per Set)

For each question set in `docs/interview/QUESTION_SETS.md`:

1. Ask baseline questions.
2. Ask follow-ups triggered by ambiguous, missing, or conflicting answers.
3. Record answers in the ledger with status:
   - `decided`
   - `assumption`
   - `open`
4. Add explicit owner for each open item.
5. Re-run only the sets with unresolved answers in the next pass.

## 3. Drafting Cadence (When to Create/Update Docs)

Drafting is **ongoing during the interview**, not a post-interview step.

Rules:
1. Create the draft tree (`docs/_draft_<project>/`) at the start of the interview (or immediately after Set 01/Set 02 baseline).
2. Update draft docs incrementally as answers become `decided`.
3. Do not “fill in” draft docs from `assumption` answers without marking the assumption explicitly and linking the open follow-up.
4. Use `docs/interview/DOCUMENT_MAPPING.md` to decide which set updates which target doc section.
5. Use reconciliation questions at the end of each pass to find missing mappings and trigger follow-ups.

## 4. Answer Quality Rules

An answer is complete only if it has:

1. Decision statement.
2. Scope boundary (in-scope vs out-of-scope).
3. Operational constraint (performance, security, compliance, cost, timeline, staffing).
4. Testability statement (how we know this works).

## 5. Iteration Triggers

Run another pass for a set if any of these occur:

1. The answer uses terms like "maybe", "later", "probably", or "TBD".
2. The answer conflicts with earlier scope or architecture choices.
3. A route/UI behavior exists without requirement coverage.
4. A requirement exists without route/data/worker implications.
5. A background process exists without execution safety semantics.

## 6. Freeze Criteria

Draft docs are ready to freeze and replace canonical `docs/` only when:

1. Every question set has all critical items marked `decided`.
2. Remaining `open` items are explicitly deferred with owner and target milestone/date.
3. Cross-document checks pass:
   - requirement -> route -> UI mapping is complete where applicable
   - requirement -> data model mapping is complete
   - async/background behavior has job execution semantics
   - testing expectations exist for all behavior changes
4. Scrub pass completes:
   - no references to the old product name
   - no leftover domain assumptions that contradict new answers
   - no stale routes/entities/constraints from the prior project

## 7. Deliverables After Freeze

1. Completed interview session file.
2. Completed answer ledger.
3. Open questions list with owners and target dates.
4. Draft-ready mapping package using `docs/interview/DOCUMENT_MAPPING.md`.
5. Scrub checklist notes (what was searched, what was removed, what remains deferred).
