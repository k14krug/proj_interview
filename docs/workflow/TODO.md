# TODO.md

Purpose: Executable task queue for this project. This file is project-specific.

Status legend:
- `[ ]` not started
- `[/]` in progress
- `[x]` complete
- `[!]` blocked

ID conventions:
- Execution-phase task: `PH-XX-YY` (execution tracking ID)
- Ad hoc reference: `AH-XX`

Terminology:
- Product Phase (V1/V2) is defined in `docs/product/PRODUCT_PHASES.md`.
- Execution Phase below is an implementation batching construct for orchestration loops.

Route conventions:
- Route IDs are defined in `docs/architecture/ROUTES_V1.md`.
- Route UI behavior is defined in `docs/architecture/UI_V1.md`.
- Every task must include `Route Links`:
  - Use `RT-*` IDs for route-affecting tasks.
  - Use `N/A` for non-route tasks.

---

## Execution Phase 01

### PH-01-01 [x] Bootstrap Flask app factory and configuration model
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`
- Requirement Links: `NFR-001`, `NFR-006`
- Route Links: `N/A`
- Scope:
  - Implement app factory structure and environment-based config loading.
  - Establish consistent dev/prod configuration shape.
- Acceptance Criteria:
  - App starts via factory in development and production entrypoints.
  - `.env` settings are loaded through one configuration layer.
- Test Requirements:
  - Add configuration loading tests for required env vars and defaults.
- Memory Bank:
  - Context: architecture requires App Factory parity.
  - Files likely touched: app package bootstrap, config module, startup scripts.
  - Risks: ad hoc config loading can diverge across environments.

### PH-01-02 [x] Establish DB connection and migration scaffolding
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `NFR-002`, `NFR-003`
- Route Links: `N/A`
- Scope:
  - Wire SQLAlchemy/Alembic baseline targeting MySQL 8.x.
  - Ensure UTC timestamp conventions are enforced in model defaults/helpers.
- Acceptance Criteria:
  - Initial migration pipeline runs cleanly.
  - DB connection and migration commands are documented and repeatable.
- Test Requirements:
  - Add minimal DB connectivity test and migration smoke test.
- Memory Bank:
  - Context: all V1 features depend on stable schema evolution.
  - Files likely touched: db bootstrap, Alembic config, migration env.
  - Risks: schema drift if migration baseline is unstable.

### PH-01-03 [x] Create baseline test harness and CI-like local command
- Owner: unassigned
- Priority: high
- Depends on: `docs/harness/testing-policy.md`
- Requirement Links: `NFR-007`
- Route Links: `N/A`
- Scope:
  - Configure pytest layout, fixtures, and mocking conventions for AI calls.
  - Define one canonical local test command for orchestrator use.
- Acceptance Criteria:
  - Test command executes and reports deterministic output.
  - AI-dependent tests run with mocks only.
- Test Requirements:
  - Add at least one passing unit test per core module scaffold.
- Memory Bank:
  - Context: orchestrated execution depends on fast, reliable feedback.
  - Files likely touched: tests package, pytest config, helper fixtures.
  - Risks: flaky tests slow phase loops and reduce trust.

---

## Execution Phase 02

### PH-02-01 [ ] Implement users and authentication model
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-001`, `FR-004`
- Route Links: `RT-01`, `RT-02`, `RT-03`
- Scope:
  - Implement `users` entity and authentication flow.
  - Associate generated artifacts to authenticated `user_id`.
- Acceptance Criteria:
  - Users can authenticate and maintain active sessions.
  - Generated entities are user-owned in storage.
- Test Requirements:
  - Add auth tests and ownership persistence tests.
  - Add integration tests covering `RT-01`, `RT-02`, `RT-03`.
- Memory Bank:
  - Context: multi-user support is V1 mandatory.
  - Files likely touched: auth services/routes, user model, session handling.
  - Risks: ownership leaks if auth and ownership are decoupled.

### PH-02-02 [ ] Implement user preferences and enforcement hooks
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-002`, `FR-003`
- Route Links: `RT-04`
- Scope:
  - Implement `user_preferences` CRUD with 1:1 per-user constraint.
  - Expose preference values to query/service filtering layers.
- Acceptance Criteria:
  - One preference record per user is enforced.
  - Preference reads are available to ingestion/cluster-view services.
- Test Requirements:
  - Add unique constraint and preference update/read tests.
  - Add integration tests covering `RT-04`.
- Memory Bank:
  - Context: filtering behavior later depends on reliable preferences.
  - Files likely touched: preference service, model, API endpoints.
  - Risks: multiple preference rows break deterministic filtering.

### PH-02-03 [ ] Enforce cross-user isolation guards in services
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-028`
- Route Links: `RT-12`, `RT-14`
- Scope:
  - Enforce same-user constraints when linking generated articles and briefings.
  - Add service guardrails to reject cross-user joins.
- Acceptance Criteria:
  - Cross-user linkage attempts are rejected consistently.
  - `briefing_articles` invariants are respected in all write paths.
- Test Requirements:
  - Add negative tests for cross-user linkage attempts.
  - Add integration tests covering authorization behavior on `RT-12` and `RT-14`.
- Memory Bank:
  - Context: DB constraints exist; service layer must match.
  - Files likely touched: briefing service, generation service, join logic.
  - Risks: silent leakage if one code path bypasses checks.

### PH-02-04 [ ] Bootstrap V1 base templates and app shell with HTMX polling pattern
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`, `docs/architecture/UI_V1.md`, `docs/architecture/ROUTES_V1.md`
- Requirement Links: `FR-001`, `FR-029`, `FR-031`
- Route Links: `RT-01`, `RT-05`, `RT-08`, `RT-13`
- Scope:
  - Establish shared server-rendered base templates (`Jinja2`) for unauthenticated and authenticated layouts.
  - Implement Bootstrap 5 shell scaffolding (top bar, left nav, main content region) for V1 routes.
  - Add reusable HTMX polling partial/pattern for async status rendering used by generation flow.
- Acceptance Criteria:
  - `RT-01` renders unauthenticated layout contract from `docs/architecture/UI_V1.md`.
  - Authenticated routes share one base shell with `Clusters`, `Preferences`, and `Briefs` navigation.
  - Polling pattern for `RT-08` is implemented as reusable template/component behavior.
- Test Requirements:
  - Add template/render tests for unauthenticated and authenticated layout contracts.
  - Add integration tests covering route rendering contracts for `RT-01`, `RT-05`, and `RT-13`.
  - Add integration test covering HTMX polling response behavior for `RT-08`.
- Memory Bank:
  - Context: V1 stack is fixed to Jinja2 + HTMX + Bootstrap 5 with minimal JS.
  - Files likely touched: base templates, shared layout partials, route view renderers, static UI assets.
  - Risks: route-specific templates can diverge without an enforced base shell pattern.

---

## Execution Phase 03

### PH-03-01 [ ] Build RSS source registry and scheduled ingestion runner
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/JOB_EXECUTION_SEMANTICS.md`
- Requirement Links: `FR-005`, `FR-006`
- Route Links: `N/A`
- Scope:
  - Implement active RSS source registry and ingestion loop.
  - Persist unique source URLs into `raw_articles`.
- Acceptance Criteria:
  - Ingestion runs on schedule and inserts expected raw items.
  - Duplicate URLs are not duplicated in storage.
- Test Requirements:
  - Add ingestion repeat-run idempotency tests.
- Memory Bank:
  - Context: ingestion is the root of all later workflows.
  - Files likely touched: ingestion services, scheduler job handlers.
  - Risks: ingestion instability blocks all downstream phases.

### PH-03-02 [ ] Implement dedupe, immutability, and full-text fetch behavior
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-007`, `FR-008`, `FR-009`
- Route Links: `N/A`
- Scope:
  - Enforce URL uniqueness and immutable raw-article insert behavior.
  - Add optional full-text fetch/status tracking where accessible.
- Acceptance Criteria:
  - Duplicate URL ingestion is safely handled.
  - Raw feed fields remain immutable after insertion.
  - Full-text status fields reflect attempt outcomes.
- Test Requirements:
  - Add dedupe and full-text status transition tests.
- Memory Bank:
  - Context: content depth directly affects generation quality.
  - Files likely touched: ingestion parsing, full-text extraction service.
  - Risks: accidental updates violate ingestion integrity.

### PH-03-03 [ ] Implement retention-safe purge command for raw data
- Owner: unassigned
- Priority: medium
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `NFR-009` (plus retention policy section 7)
- Route Links: `N/A`
- Scope:
  - Implement purge job using `NOT EXISTS` safeguards against lineage/audit tables.
  - Restrict purge to allowed tables/conditions.
- Acceptance Criteria:
  - Referenced source rows are never deleted.
  - Purge logs row counts and handles re-runs safely.
- Test Requirements:
  - Add purge safety tests for referenced vs unreferenced rows.
- Memory Bank:
  - Context: purge must preserve immutable provenance.
  - Files likely touched: cleanup job, SQL query layer, ops logging.
  - Risks: lineage breakage if query safeguards regress.

---

## Execution Phase 04

### PH-04-01 [ ] Implement event clustering assignment pipeline
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-010`, `FR-011`
- Route Links: `N/A`
- Scope:
  - Implement similarity-based clustering into `clusters` + `cluster_articles`.
  - Maintain cached cluster metadata (`article_count`, timestamps).
- Acceptance Criteria:
  - Similar articles form consistent cluster groups.
  - Re-runs do not create duplicate cluster links.
- Test Requirements:
  - Add clustering idempotency and assignment tests.
- Memory Bank:
  - Context: cluster quality drives manual selection and generation outcomes.
  - Files likely touched: clustering service, cluster models, scheduler job.
  - Risks: weak similarity thresholds create noisy clusters.

### PH-04-02 [ ] Implement cluster list/detail views with sorting
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`
- Requirement Links: `FR-012`, `FR-013`, `FR-014`
- Route Links: `RT-05`, `RT-06`
- Scope:
  - Implement user-visible cluster list and source-article detail views.
  - Support recency/source-count sorting.
- Acceptance Criteria:
  - Cluster lists are sortable and browsable for manual review.
  - Cluster detail provides source-article context for selection.
- Test Requirements:
  - Add API/view tests for sorting and visibility.
  - Add integration tests covering `RT-05` and `RT-06`.
- Memory Bank:
  - Context: this is the primary editorial decision surface in V1.
  - Files likely touched: cluster API routes, templates/front-end views.
  - Risks: poor sorting can bury important events.

### PH-04-03 [ ] Enforce user preference filtering and information gap indicators
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-013A`, `FR-013B`, `FR-013C`, `FR-013D`
- Route Links: `RT-05`, `RT-06`
- Scope:
  - Apply per-user source preference filtering to cluster views.
  - Compute and surface information gap labels/scores.
- Acceptance Criteria:
  - Blacklisted sources are hidden per user in cluster detail.
  - Information gap labels appear in list/detail views.
- Test Requirements:
  - Add filtering and indicator-label tests.
  - Add integration tests covering filtered output behavior on `RT-05` and `RT-06`.
- Memory Bank:
  - Context: trust depends on relevance and transparent source depth.
  - Files likely touched: query filters, cluster scoring logic, UI rendering.
  - Risks: global clusters can feel incorrect without user-level filtering.

---

## Execution Phase 05

### PH-05-01 [ ] Implement async generation lifecycle and worker handoff
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`, `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-029`, `FR-030`, `FR-031`, `NFR-010`
- Route Links: `RT-07`, `RT-08`
- Scope:
  - Implement queued/running/success/failed lifecycle for generated articles.
  - Route generation execution through background worker flow.
- Acceptance Criteria:
  - Generate request returns quickly and enters queued state.
  - Worker updates lifecycle status transitions correctly.
- Test Requirements:
  - Add lifecycle transition tests and polling behavior tests.
  - Add integration tests covering `RT-07` and `RT-08`.
- Memory Bank:
  - Context: async flow avoids timeout-heavy request paths.
  - Files likely touched: generation endpoints, worker handlers, status APIs.
  - Risks: race conditions can leave tasks stuck in running.

### PH-05-02 [ ] Implement prompt construction with source-only boundaries
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`
- Requirement Links: `FR-016`, `FR-016A`, `FR-016B`, `FR-020`, `FR-021`
- Route Links: `N/A`
- Scope:
  - Construct prompts from selected sources only.
  - Apply accuracy-over-length policy and low-information mode.
- Acceptance Criteria:
  - Prompt payload contains only selected source context.
  - Low-information mode behavior is invoked when source depth is thin.
- Test Requirements:
  - Add prompt-construction tests for normal and low-information inputs.
- Memory Bank:
  - Context: this is primary defense against hallucinated filler.
  - Files likely touched: ai service prompt builder, generation orchestrator.
  - Risks: prompt drift can weaken source-only guarantees.

### PH-05-03 [ ] Implement generated article content fields and summary bullet
- Owner: unassigned
- Priority: medium
- Depends on: `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-022`, `FR-022A`, `FR-023`, `FR-024`
- Route Links: `RT-09`
- Scope:
  - Persist generated headline/body/summary with immutability semantics.
  - Ensure summary bullet links to full article.
- Acceptance Criteria:
  - Finalized content fields are immutable post-success.
  - Summary bullets are generated and routable to full content.
- Test Requirements:
  - Add immutability and summary-link tests.
  - Add integration tests covering `RT-09`.
- Memory Bank:
  - Context: article UX requires consistent immutable snapshots.
  - Files likely touched: generation persistence, article views.
  - Risks: improper updates can violate editorial traceability.

---

## Execution Phase 06

### PH-06-01 [ ] Implement citation validation and source mapping gates
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/ARCHITECTURE.md`
- Requirement Links: `FR-017`, `FR-018`, `FR-019`
- Route Links: `RT-07`, `RT-09`
- Scope:
  - Parse/validate inline citations against selected source set.
  - Reject/regenerate or fail generation when validation fails.
- Acceptance Criteria:
  - Invalid citation mappings cannot reach success state.
  - Validation failures are logged with actionable error data.
- Test Requirements:
  - Add positive/negative citation mapping tests.
  - Add integration tests confirming invalid citation flows fail through `RT-07`/`RT-09` semantics.
- Memory Bank:
  - Context: source-only enforcement is central product trust control.
  - Files likely touched: citation parser, generation validator.
  - Risks: weak parsing creates false positives/negatives.

### PH-06-02 [ ] Persist lineage and citation provenance tables
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-032`, `FR-033`, `FR-034`
- Route Links: `N/A`
- Scope:
  - Populate `generated_article_sources` and `generated_article_citations`.
  - Record provenance status and optional excerpt evidence.
- Acceptance Criteria:
  - Successful generations persist complete source lineage.
  - Citation provenance records are queryable for audit UI.
- Test Requirements:
  - Add lineage/provenance insert and integrity tests.
- Memory Bank:
  - Context: immutable auditability requires durable provenance rows.
  - Files likely touched: generation persistence and citation storage logic.
  - Risks: missing provenance undermines audit panel value.

### PH-06-03 [ ] Build V1-lite synthesis audit view/API
- Owner: unassigned
- Priority: medium
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/architecture/ARCHITECTURE.md`
- Requirement Links: `FR-032`, `FR-033`, `FR-034`
- Route Links: `RT-10`
- Scope:
  - Build citation-to-source audit UI/API with excerpt when available.
  - Clearly label source-only citations when excerpt is unavailable.
- Acceptance Criteria:
  - Users can inspect citation -> source mapping per generated article.
  - Provenance status is displayed unambiguously.
- Test Requirements:
  - Add response-shape tests and UI rendering tests for each provenance status.
  - Add integration tests covering `RT-10`.
- Memory Bank:
  - Context: audit view converts trust requirements into visible product behavior.
  - Files likely touched: audit endpoints, templates/UI components.
  - Risks: unclear labels can overstate confidence.

---

## Execution Phase 07

### PH-07-01 [ ] Implement daily brief creation and ordering
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-025`, `FR-026`, `FR-027`
- Route Links: `RT-11`, `RT-12`, `RT-13`, `RT-14`
- Scope:
  - Implement briefing creation from selected generated articles.
  - Preserve ordering with immutable snapshot semantics.
- Acceptance Criteria:
  - Users can build 10-15 article briefings.
  - Brief ordering is persisted and stable.
- Test Requirements:
  - Add briefing creation/order immutability tests.
  - Add integration tests covering `RT-11`, `RT-12`, `RT-13`, and `RT-14`.
- Memory Bank:
  - Context: briefing is the core output artifact for V1.
  - Files likely touched: briefing service, join table writes, briefing views.
  - Risks: ordering bugs degrade reader usefulness.

### PH-07-02 [ ] Enforce same-user constraints across briefing workflows
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/DATA_MODEL.md`
- Requirement Links: `FR-028`
- Route Links: `RT-12`, `RT-13`, `RT-14`
- Scope:
  - Enforce same-user joins in all briefing operations.
  - Reject cross-user add/remove operations consistently.
- Acceptance Criteria:
  - Cross-user operations fail with clear errors.
  - DB/service constraints remain aligned.
- Test Requirements:
  - Add negative authorization tests for briefing actions.
  - Add integration tests covering access constraints on `RT-12`, `RT-13`, and `RT-14`.
- Memory Bank:
  - Context: isolation must hold at service and schema layers.
  - Files likely touched: briefing service, API handlers, permission checks.
  - Risks: one missed path can expose other user content.

### PH-07-03 [ ] Build end-to-end editorial workflow UI pass
- Owner: unassigned
- Priority: medium
- Depends on: `docs/architecture/ARCHITECTURE.md`, `docs/product/REQUIREMENTS.md`
- Requirement Links: `FR-014`, `FR-015`, `FR-025`, `FR-031`
- Route Links: `RT-05`, `RT-06`, `RT-07`, `RT-08`, `RT-09`, `RT-10`, `RT-11`, `RT-12`, `RT-13`, `RT-14`
- Scope:
  - Ensure coherent UX across cluster review -> generate -> audit -> briefing.
  - Normalize loading/error states and navigation between steps.
- Acceptance Criteria:
  - End-to-end workflow is operable without admin-only shortcuts.
  - UI reflects async processing and task outcomes clearly.
- Test Requirements:
  - Add integration tests for core editorial workflow path.
- Memory Bank:
  - Context: V1 success depends on operational usability, not just backend correctness.
  - Files likely touched: route/controller wiring, templates/frontend views.
  - Risks: fragmented UX slows human-in-the-loop operation.

---

## Execution Phase 08

### PH-08-01 [ ] Implement worker job-run slot-claim and overlap protection
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/JOB_EXECUTION_SEMANTICS.md`
- Requirement Links: `NFR-008`, `NFR-009`
- Route Links: `N/A`
- Scope:
  - Implement job slot claims using `job_runs(job_name, scheduled_for)`.
  - Enforce `max_instances=1` and stale-run handling.
- Acceptance Criteria:
  - Duplicate schedule-slot executions are prevented.
  - Stale-running rows are handled per semantics.
- Test Requirements:
  - Add slot-claim, overlap, and stale-run tests.
- Memory Bank:
  - Context: job correctness is essential for ingestion and clustering trust.
  - Files likely touched: worker scheduler wiring, job-run repository logic.
  - Risks: subtle race conditions during recovery windows.

### PH-08-02 [ ] Implement startup recovery routine for abandoned running jobs
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/JOB_EXECUTION_SEMANTICS.md`
- Requirement Links: `NFR-008`, `NFR-009`
- Route Links: `N/A`
- Scope:
  - On worker boot, reconcile stale `running` rows for prior instance.
  - Mark failed with recovery reason before schedule loop starts.
- Acceptance Criteria:
  - Recovery executes once at startup and logs outcomes.
  - Abandoned rows do not block future schedule slots.
- Test Requirements:
  - Add restart/recovery tests with simulated crash state.
- Memory Bank:
  - Context: this addresses ghost-worker failure mode explicitly.
  - Files likely touched: worker bootstrap, recovery service.
  - Risks: false recovery on active jobs if identity logic is weak.

### PH-08-03 [ ] Add structured ops logging and generation traceability fields
- Owner: unassigned
- Priority: medium
- Depends on: `docs/architecture/DATA_MODEL.md`, `docs/product/REQUIREMENTS.md`
- Requirement Links: `NFR-007`
- Route Links: `N/A`
- Scope:
  - Ensure prompt/response metadata and error details are logged consistently.
  - Add operational logs for ingestion, clustering, and generation transitions.
- Acceptance Criteria:
  - Failed and successful generation attempts are traceable by request/job IDs.
  - Ops logs include enough detail for troubleshooting.
- Test Requirements:
  - Add tests for trace record persistence on success/failure paths.
- Memory Bank:
  - Context: observability is mandatory for reliable multi-step workflows.
  - Files likely touched: AI service logging, worker/job logging utilities.
  - Risks: under-logged failures are hard to diagnose post hoc.

---

## Execution Phase 09

### PH-09-01 [ ] Production deployment hardening and runbook finalization
- Owner: unassigned
- Priority: high
- Depends on: `docs/architecture/ARCHITECTURE.md`
- Requirement Links: `NFR-001`, `NFR-002`, `NFR-005`, `NFR-006`
- Route Links: `N/A`
- Scope:
  - Finalize web/worker service setup, reverse proxy, and tunnel configuration docs.
  - Document startup, restart, backup, and recovery procedures.
- Acceptance Criteria:
  - Deployment instructions are repeatable end-to-end.
  - Web and worker separation is explicit and verified.
- Test Requirements:
  - Add deployment smoke checklist and execute it once.
- Memory Bank:
  - Context: V1 requires secure external access with local DB boundaries.
  - Files likely touched: deployment scripts/config docs/runbooks.
  - Risks: misconfiguration can duplicate jobs or expose unsafe endpoints.

### PH-09-02 [ ] Requirement coverage audit and V1 acceptance verification
- Owner: unassigned
- Priority: high
- Depends on: `docs/product/REQUIREMENTS.md`, `docs/workflow/PROGRESS.md`
- Requirement Links: `FR-001`-`FR-034`, `NFR-001`-`NFR-010`
- Route Links: `N/A`
- Scope:
  - Build final traceability matrix from tasks/tests to FR/NFR items.
  - Validate V1 success criteria checklist with evidence links.
- Acceptance Criteria:
  - Every FR/NFR has implementation/test evidence or explicit exception note.
  - Success criteria section is confirmed or blockers are documented.
- Test Requirements:
  - No new feature tests required; verify and catalog existing coverage.
- Memory Bank:
  - Context: final sign-off should be requirement-driven, not intuition-driven.
  - Files likely touched: audit report doc, workflow logs, requirement references.
  - Risks: hidden coverage gaps can delay release readiness.

### PH-09-03 [ ] V1 freeze, backlog triage, and Phase 2 parking lot handoff
- Owner: unassigned
- Priority: medium
- Depends on: `docs/product/PRODUCT_PHASES.md`, `docs/workflow/TODO_template.md`
- Requirement Links: `N/A` (project management handoff)
- Route Links: `N/A`
- Scope:
  - Freeze V1 task set and move unresolved non-V1 ideas to Phase 2 parking lot.
  - Prepare clean start point for next orchestrator cycle.
- Acceptance Criteria:
  - V1 backlog is stable and no active scope bleed remains.
  - Phase 2 candidates are documented without executable V1 tasks.
- Test Requirements:
  - N/A (documentation/process task)
- Memory Bank:
  - Context: final phase protects V1 completion discipline.
  - Files likely touched: TODO, roadmap/parking lot docs, progress log.
  - Risks: untriaged tasks can reintroduce ambiguous scope.

---

## Notes
- Keep tasks small and independently shippable.
- Every behavior-changing task should include tests when testable.
- If a task changes behavior but no tests are added, record explicit rationale in `docs/workflow/PROGRESS.md`.
