# Interview Process

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

## 3. Answer Quality Rules

An answer is complete only if it has:

1. Decision statement.
2. Scope boundary (in-scope vs out-of-scope).
3. Operational constraint (performance, security, compliance, cost, timeline, staffing).
4. Testability statement (how we know this works).

## 4. Iteration Triggers

Run another pass for a set if any of these occur:

1. The answer uses terms like "maybe", "later", "probably", or "TBD".
2. The answer conflicts with earlier scope or architecture choices.
3. A route/UI behavior exists without requirement coverage.
4. A requirement exists without route/data/worker implications.
5. A background process exists without execution safety semantics.

## 5. Freeze Criteria

Interview is ready for drafting only when:

1. Every question set has all critical items marked `decided`.
2. Remaining `open` items are explicitly deferred with owner and phase.
3. Cross-document checks pass:
   - requirement -> route -> UI mapping is complete where applicable
   - requirement -> data model mapping is complete
   - async/background behavior has job execution semantics
   - testing expectations exist for all behavior changes

## 6. Deliverables After Freeze

1. Completed interview session file.
2. Completed answer ledger.
3. Open questions list with owners and target dates.
4. Draft-ready mapping package using `docs/interview/DOCUMENT_MAPPING.md`.
