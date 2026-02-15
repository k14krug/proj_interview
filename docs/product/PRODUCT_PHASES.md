# Scope Guardrails (Template)

Project: `<ProjectName>`
Doc Status: `template` | `draft` | `frozen`
Last Updated (UTC): `<YYYY-MM-DD>`

Note: This file name is historical. Treat it as the canonical place for **V1 vs not-V1** scope guardrails and future-readiness principles, without assuming a phased roadmap.

## 1. V1 Boundary Statement

- What V1 is (one paragraph):
- What V1 is not (one paragraph):

## 2. Exclusion Guardrails (Anti-Scope Rules)

Hard “do not build yet” rules that prevent accidental scope creep.

Examples (replace with real rules):
- Do not add roles/permissions beyond what is explicitly required in V1.
- Do not introduce background job orchestration beyond the semantics in `docs/architecture/JOB_EXECUTION_SEMANTICS.md`.
- Do not add multi-tenant abstractions unless V1 requires them.

## 3. Future-Readiness Principles

Constraints V1 must respect so future capabilities remain possible:
- Data model extensibility rules:
- Route contract stability rules:
- UI contract extensibility rules:

## 4. Deferred Decisions (Milestone/Date Based)

| ID | Decision | Deferred Until (Milestone/Date) | Rationale | Risk |
|---|---|---|---|---|
| DD-001 | TBD | TBD | TBD | TBD |

