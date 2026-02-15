# Project Interview Kit

Reusable interview framework for gathering complete project inputs before implementation.

This repository provides a structured, multi-pass interview process that helps you turn stakeholder answers into a full technical documentation set (requirements, architecture, routes/UI contracts, data model, execution semantics, and workflow governance).

Concrete example docs snapshots live in `docs/examples/`. The canonical `docs/` paths are templates intended to be replaced per-project after running the interview.

## Start Here

1. Open `docs/interview/README.md`.
2. Run the interview flow in `docs/interview/INTERVIEW_PROCESS.md`.
3. Use staged prompts in `docs/interview/QUESTION_SETS.md`.
4. Track answers with:
   - `docs/interview/INTERVIEW_SESSION_TEMPLATE.md`
   - `docs/interview/ANSWER_LEDGER_TEMPLATE.md`
5. Draft final docs using `docs/interview/DOCUMENT_MAPPING.md`.

## New Project Quick Start (Copy/Paste Prompt)

Paste this as your first message to the agent to start a new project with this repo:

```text
/INTERVIEW <ProjectName>

Goal: Use this repository as a documentation template to produce a complete new docs set for <ProjectName>.

Hard rules:
- This is a documentation process, not a coding process. Do not change application code during the interview.
- Do not modify AGENTS.md unless I explicitly approve it in this chat.

Drafting rules:
- Create `docs/_draft_<ProjectName>/` and draft continuously during the interview, updating only from `decided` answers.
- Keep canonical `docs/` files as-is until freeze criteria are met; only then replace `docs/` with the finalized draft.
- Run a scrub pass to remove any inherited names/assumptions from the draft before freeze.

Start with Set 01 and ask questions one at a time. Record each answer in the ledger with status (`decided` / `assumption` / `open`) and an owner for each `open` item.
```

## Recommended Workflow

1. Run pass 1 for baseline answers.
2. Loop on follow-up questions where answers are ambiguous or conflicting.
3. Resolve cross-set conflicts (requirements vs routes, routes vs UI, data vs retention).
4. Freeze when critical decisions are explicit and testable.

## Core Principle

Do not draft implementation docs from assumptions.  
Capture decisions, constraints, and validation expectations first, then draft.
