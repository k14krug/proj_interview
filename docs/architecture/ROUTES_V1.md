# ROUTES_V1.md

Project: K2 Daily Brief

Purpose: Canonical V1 route contract for UI/API behavior.  
If implementation uses equivalent API prefixes (for example `/api/...`) the same route semantics must be preserved.
Detailed screen/layout behavior is defined in `docs/architecture/UI_V1.md`.

---

## Route IDs

### RT-01 Login View
- Method/Path: `GET /login`
- Purpose: Render authentication entry page.
- Requirement Links: `FR-001`

### RT-02 Login Action
- Method/Path: `POST /login`
- Purpose: Authenticate user and start session.
- Requirement Links: `FR-001`

### RT-03 Logout Action
- Method/Path: `POST /logout`
- Purpose: End authenticated session.
- Requirement Links: `FR-001`

### RT-15 User Registration View
- Method/Path: `GET /register`
- Purpose: Render new-user creation form.
- Requirement Links: `FR-001`, `FR-001A`, `FR-001B`, `FR-001C`

Notes:
- V1 safety rule: this view is only available when either:
	- no users exist yet (first-user bootstrap), OR
	- registration is explicitly enabled by operator policy.

### RT-16 User Registration Action
- Method/Path: `POST /register`
- Purpose: Create a new user account.
- Requirement Links: `FR-001`, `FR-001A`, `FR-001B`, `FR-001C`

Notes:
- On success, redirect to `RT-01` (login) or auto-login per implementation decision.
- On failure (duplicate email, invalid password), re-render `RT-15` with inline errors.
- If the implementation uses pending-user caching, the account must be activated within 48 hours or it expires.

### RT-04 Preferences View/Update
- Method/Path: `GET /preferences`, `POST /preferences`
- Purpose: View/update user topic/source preferences and show user-scoped daily API usage cost reporting.
- Requirement Links: `FR-002`, `FR-003`, `FR-035`, `FR-036`, `FR-040`, `FR-041`

### RT-05 Cluster List
- Method/Path: `GET /clusters`
- Purpose: Show cluster list with sorting and Information Gap indicator.
- Requirement Links: `FR-012`, `FR-013`, `FR-013C`, `FR-013D`

### RT-06 Cluster Detail
- Method/Path: `GET /clusters/{cluster_id}`
- Purpose: Show cluster source articles with per-user filtering and manual selection context.
- Requirement Links: `FR-013A`, `FR-013B`, `FR-014`, `FR-015`

### RT-07 Generation Request
- Method/Path: `POST /clusters/{cluster_id}/generate`
- Purpose: Trigger async generation for selected sources.
- Requirement Links: `FR-016`, `FR-029`

### RT-08 Generation Status
- Method/Path: `GET /generated-articles/{article_id}/status`
- Purpose: Return lifecycle state (`queued`, `running`, `success`, `failed`) for polling UX.
- Requirement Links: `FR-030`, `FR-031`

### RT-09 Generated Article View
- Method/Path: `GET /generated-articles/{article_id}`
- Purpose: Display finalized generated article and summary bullet.
- Requirement Links: `FR-022`, `FR-023`, `FR-024`

### RT-10 Synthesis Audit View
- Method/Path: `GET /generated-articles/{article_id}/audit`
- Purpose: Show citation -> source mapping with provenance status and optional excerpts.
- Requirement Links: `FR-032`, `FR-033`, `FR-034`

### RT-11 Brief Composer View
- Method/Path: `GET /briefs/new`
- Purpose: Present generated article selection for brief compilation.
- Requirement Links: `FR-025`

### RT-12 Brief Create Action
- Method/Path: `POST /briefs`
- Purpose: Create immutable Daily Brief snapshot.
- Requirement Links: `FR-025`, `FR-026`, `FR-028`

### RT-13 Brief List View
- Method/Path: `GET /briefs`
- Purpose: List user briefs by date/time.
- Requirement Links: `FR-027`

### RT-14 Brief Detail View
- Method/Path: `GET /briefs/{brief_id}`
- Purpose: Display immutable Daily Brief snapshot content.
- Requirement Links: `FR-026`, `FR-027`

---

## Coverage Rule
- Any TODO task that changes UI/API behavior must include `Route Links` referencing `RT-*` IDs from this file.
- Route-linked tasks must include integration tests for the linked route semantics.
