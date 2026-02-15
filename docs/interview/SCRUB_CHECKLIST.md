# Scrub Checklist (Template Hygiene)

Purpose: when using this repository as a starting point for a new project, prevent accidental carry-over of the prior project's identity, assumptions, and domain specifics.

This checklist applies to:
1. Your draft tree (`docs/_draft_<project>/`), before freeze.
2. Any “starter-kit” snapshot you intend to reuse for future projects.

## 1. Decide: Example vs Template

Pick one of these patterns and be consistent:

- **Template-first (recommended):** canonical docs under `docs/` are generic placeholders; keep any prior project docs under `docs/examples/<example_project>/`.
- **Example-in-place:** canonical docs under `docs/` remain a concrete prior project example, but must be clearly labeled “example” and you must always draft into `docs/_draft_<project>/` for new work.

## 2. Identity Scrub

Search and replace across the draft tree for:

- Old project name(s), abbreviations, codenames
- Old domain nouns (entity names, workflows, route names) that do not exist in the new project
- Old environment names/hosts/regions
- Old integrations/providers

Record what you searched for and what you changed in your interview session notes.

## 3. Assumption Scrub

Confirm the draft tree does **not** implicitly inherit:

- A specific frontend framework, unless decided
- A specific backend framework, unless decided
- A specific job system, unless decided
- A “phased roadmap” assumption beyond “V1 vs not-V1”
- A specific multi-tenant model, unless decided

## 4. Consistency Scrub

Run cross-document checks:

- Each requirement maps to routes and UI (where applicable)
- Each route maps back to requirements
- Each entity/relationship appears in requirements and workflows where used
- Background jobs have explicit execution safety semantics

## 5. Final Gate (Before Freeze)

Before replacing `docs/` with the draft:

1. Confirm no old project identifiers remain in `docs/_draft_<project>/`.
2. Confirm deferred items have owner + milestone/date.
3. Confirm `AGENTS.md` is unchanged, unless you explicitly approved a change.

