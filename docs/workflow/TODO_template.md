# TODO.md (Template Copy)

Use this file as a starting point for `docs/workflow/TODO.md` when initializing a new project.

See `docs/harness/commands.md` for `/TASK`, `/PHASE`, and `/INTERVIEW` execution rules.

---

## Execution Phase 01

### PH-01-01 [ ] Conduct documentation interview and draft docs set
- Owner: unassigned
- Priority: high
- Depends on: `docs/interview/` kit
- Requirement Links: `N/A` (documentation-only)
- Route Links: `N/A`
- Scope:
  - Run `/INTERVIEW [ProjectName]` per `docs/harness/commands.md`.
  - Draft the new docs set into `docs/_draft_<ProjectName>/`.
  - Complete scrub pass per `docs/interview/SCRUB_CHECKLIST.md`.
- Acceptance Criteria:
  - Interview artifacts exist in `docs/interview/` and are project-named.
  - Draft tree `docs/_draft_<ProjectName>/` exists with filled docs.
  - `docs/_draft_<ProjectName>/workflow/TODO.md` is fully populated and implementation-ready (not template-only).
  - Scrub pass checklist is satisfied.
  - `./scripts/validate_docs.sh` passes.
- Test Requirements:
  - Run `./scripts/validate_docs.sh`.
- Memory Bank:
  - Context:
    - This task exists to prevent starting implementation before docs are frozen.
  - Risks:
    - Skipping doc freeze causes scope drift and inconsistent contracts.
