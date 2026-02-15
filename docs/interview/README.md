# Project Interview Kit

Purpose: run a structured interview that gathers enough information to create a complete implementation-ready docs set for a new software project.

This kit is designed for iterative interviewing, not one-shot questionnaires. You ask in sets, follow up on gaps, resolve conflicts, then draft docs.

This is a **documentation process**, not a coding process. Do not change application code during the interview unless you explicitly pause the interview and approve implementation work.

## Who This Is For

Use this if you are:

1. Starting a new project from scratch.
2. Re-scoping an existing project into a disciplined V1.
3. Working with an AI/coding agent and need consistent product + architecture + workflow inputs.

## What You Get

Completed interviews should produce draft-ready inputs for:

1. Product requirements and scope boundaries.
2. Architecture, data model, routes, and UI contracts.
3. Background-job execution semantics.
4. Delivery harness docs (commands, testing policy, task handshake).
5. Execution workflow docs (`TODO` and `PROGRESS` style operating docs).

## Directory Contents

1. `INTERVIEW_PROCESS.md` - pass-based method and quality gates.
2. `QUESTION_SETS.md` - staged question sets with follow-up triggers.
3. `DOCUMENT_MAPPING.md` - exact mapping from answers to target docs.
4. `INTERVIEW_SESSION_TEMPLATE.md` - run tracker for a project interview.
5. `ANSWER_LEDGER_TEMPLATE.md` - detailed answer ledger with open/assumption tracking.

## How To Use

1. Create interview artifacts in `docs/interview/`:
   - Copy `INTERVIEW_SESSION_TEMPLATE.md`.
   - Copy `ANSWER_LEDGER_TEMPLATE.md`.
   - Rename both files to include the new project's name (for example: `AcmeWidget_INTERVIEW_SESSION.md`, `AcmeWidget_ANSWER_LEDGER.md`).
2. Run the question sets in `QUESTION_SETS.md` in order, revisiting sets when follow-up triggers fire.
3. Record answers in the ledger with status (`decided` / `assumption` / `open`) and an owner for every `open` item.
4. Draft into a **parallel tree** (recommended): create `docs/_draft_<project>/` early and update it continuously as answers become `decided` (see `INTERVIEW_PROCESS.md`).
5. Scrub old product names/assumptions from **all drafted docs** before freeze (see `INTERVIEW_PROCESS.md` and `SCRUB_CHECKLIST.md`).
6. Freeze only when critical items are `decided`, then replace the canonical docs under `docs/` with the finalized draft.

Tip: if using the harness slash commands, start with `/INTERVIEW [ProjectName]` (defined in `docs/harness/commands.md`).

## Working Pattern

Use a four-pass cadence:

1. Baseline discovery.
2. Constraint and edge-case probing.
3. Conflict resolution and tradeoff decisions.
4. Freeze and drafting handoff.

## Output Quality Standard

A usable answer has all four:

1. Decision statement.
2. Scope boundary.
3. Operational constraint.
4. Testability statement.
