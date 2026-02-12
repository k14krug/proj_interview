# Project Interview Kit

Purpose: run a structured interview that gathers enough information to create a complete implementation-ready docs set for a new software project.

This kit is designed for iterative interviewing, not one-shot questionnaires. You ask in sets, follow up on gaps, resolve conflicts, then draft docs.

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
4. `templates/INTERVIEW_SESSION_TEMPLATE.md` - run tracker for a project interview.
5. `templates/ANSWER_LEDGER_TEMPLATE.md` - detailed answer ledger with open/assumption tracking.

## How To Use

1. Copy `templates/INTERVIEW_SESSION_TEMPLATE.md` for your new project.
2. Copy `templates/ANSWER_LEDGER_TEMPLATE.md` for answer tracking.
3. Run Set 01 through Set 10 in `QUESTION_SETS.md`.
4. Re-run only sets with unresolved or conflicting answers.
5. Apply `DOCUMENT_MAPPING.md` to draft your final docs.
6. Freeze decisions only when critical items are `decided`.

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
