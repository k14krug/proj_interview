# Project Interview Kit

Reusable interview framework for gathering complete project inputs before implementation.

This repository provides a structured, multi-pass interview process that helps you turn stakeholder answers into a full technical documentation set (requirements, architecture, routes/UI contracts, data model, execution semantics, and workflow governance).

## Start Here

1. Open `docs/interview/README.md`.
2. Run the interview flow in `docs/interview/INTERVIEW_PROCESS.md`.
3. Use staged prompts in `docs/interview/QUESTION_SETS.md`.
4. Track answers with:
   - `docs/interview/templates/INTERVIEW_SESSION_TEMPLATE.md`
   - `docs/interview/templates/ANSWER_LEDGER_TEMPLATE.md`
5. Draft final docs using `docs/interview/DOCUMENT_MAPPING.md`.

## Recommended Workflow

1. Run pass 1 for baseline answers.
2. Loop on follow-up questions where answers are ambiguous or conflicting.
3. Resolve cross-set conflicts (requirements vs routes, routes vs UI, data vs retention).
4. Freeze when critical decisions are explicit and testable.

## Core Principle

Do not draft implementation docs from assumptions.  
Capture decisions, constraints, and validation expectations first, then draft.
