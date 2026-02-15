# TODO.md

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

### PH-01-01 [ ] Define Information Gap Scoring Formula (V1)
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-013C`, `FR-013D`
- Route Links: `N/A`
- Scope:
  - Define a deterministic V1 scoring formula for `info_gap_label` (`thin`, `moderate`, `high_depth`).
  - Document formula inputs, weights, and thresholds.
- Acceptance Criteria:
  - Inputs and weights are explicitly documented.
  - Thresholds for each label are explicit and testable.
  - No Phase 2 logic introduced.
- Test Requirements:
  - Add unit tests for at least one example cluster in each label bucket.
- Memory Bank:
  - Context:
    - V1 requires indicator visibility but the exact formula is not finalized.
  - Files likely touched:
    - `docs/architecture/ARCHITECTURE.md`
    - `docs/product/REQUIREMENTS.md`
    - `docs/architecture/DATA_MODEL.md`
  - Risks:
    - Ambiguous thresholds can create inconsistent editorial outcomes.

### PH-01-02 [ ] Synthesis Audit UI Contract (V1-lite)
- Owner: unassigned
- Priority: medium
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/DATA_MODEL.md`, `docs/architecture/ARCHITECTURE.md`
- Requirement Links: `FR-032`, `FR-033`, `FR-034`
- Route Links: `RT-10`
- Scope:
  - Define API/UI response contract for citation-to-source mapping.
  - Include excerpt handling when provenance exists.
- Acceptance Criteria:
  - Contract includes citation label, source URL, provenance status, optional excerpt.
  - Explicit behavior when excerpt is unavailable.
- Test Requirements:
  - Add API/service tests for one `verified_excerpt` case and one `source_only` case.
- Memory Bank:
  - Context:
    - V1-lite audit is required; exact character highlighting is Phase 2.
  - Files likely touched:
    - `docs/architecture/ARCHITECTURE.md`
    - `docs/architecture/DATA_MODEL.md`
    - service/API docs or code
  - Risks:
    - Drift between stored citation provenance and UI rendering expectations.

### PH-01-03 [ ] Worker Startup Recovery Implementation
- Owner: unassigned
- Priority: medium
- Depends on: `docs/architecture/JOB_EXECUTION_SEMANTICS.md`
- Requirement Links: `NFR-008`, `NFR-009`
- Route Links: `N/A`
- Scope:
  - Implement startup reconciliation for stale `job_runs.status='running'`.
- Acceptance Criteria:
  - Worker marks stale rows failed with recovery reason at boot.
  - Behavior is covered by tests.
- Test Requirements:
  - Add restart/recovery test for stale job row handling.
- Memory Bank:
  - Context:
    - Semantics are documented; implementation is pending.
  - Risks:
    - Duplicate work or stuck jobs if startup recovery is absent.

---

## Execution Phase 02

### PH-02-01 [ ] Placeholder for Next Planned Reader-Mode Task
- Owner: unassigned
- Priority: low
- Depends on: `docs/product/PRODUCT_PHASES.md`
- Requirement Links: `TBD` (Phase 2 requirements not yet defined in `docs/product/REQUIREMENTS.md`)
- Route Links: `N/A`
- Scope:
  - Replace this placeholder only when Phase 1 scope is complete and approved.
- Acceptance Criteria:
  - Explicit user approval for Phase 2 work is recorded.
- Test Requirements:
  - Define tests when real scope is added.
- Memory Bank:
  - Context:
    - Phase 2 work must not begin without explicit approval.
  - Risks:
    - Scope bleed into Reader Mode.

---

## Notes
- Keep tasks small and independently shippable.
- Every behavior-changing task should include tests when testable.
