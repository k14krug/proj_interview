# TODO (Template)

Purpose: Task queue and memory-bank context for agent handoffs.

Status legend:
- `[ ]` not started
- `[/]` in progress
- `[x]` complete
- `[!]` blocked

ID conventions:
- Execution-phase task: `PH-XX-YY` (execution tracking ID)
- Ad hoc reference: `AH-XX`

Route conventions:
- Route IDs are defined in `docs/architecture/ROUTES_V1.md`.
- Route UI behavior is defined in `docs/architecture/UI_V1.md`.
- Every task must include `Route Links`:
  - Use `RT-*` IDs for route-affecting tasks.
  - Use `N/A` for non-route tasks.

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
    - New projects should not inherit identity/assumptions from prior examples.
  - Files likely touched:
    - `docs/interview/*`
    - `docs/_draft_<ProjectName>/*`
  - Risks:
    - Incomplete requirements or route/UI mapping will cause rework during implementation.

---

## Notes
- Keep tasks small and independently shippable.
- Every behavior-changing task should include tests when testable.
