# UI_V1.md
Project: K2 Daily Brief

Purpose: Canonical V1 UI contract for layout, route-level behavior, and interaction states.

---

## 1. Scope

This document defines only V1 "Newsroom Engine" UI behavior.

In scope:
- Route-level UI contracts aligned to `docs/architecture/ROUTES_V1.md`.
- Layout, navigation, and shared UI component behavior.
- Async generation UX and audit visibility requirements.

Out of scope:
- Reader Mode simplification (Phase 2).
- Character-level source span highlighting in article body text.
- New routes beyond the V1 route contract.

---

## 2. UI Technology Decision (V1)

V1 frontend stack is intentionally simple and server-first.

Required technologies:
- Flask server-rendered templates (`Jinja2`) for all screen routes.
- `HTMX` for partial page updates and polling interactions (especially `RT-08` status polling).
- `Bootstrap 5` for baseline layout/grid/forms/components.
- Small, page-scoped vanilla JavaScript only when HTMX is insufficient.

Implementation constraints:
- No single-page app framework in V1 (`React`, `Vue`, `Angular` are out of scope).
- No client-side router; canonical navigation follows server routes in `docs/architecture/ROUTES_V1.md`.
- Keep JavaScript minimal and focused on UX state glue, not business logic.
- Business rules stay in backend services per `docs/architecture/ARCHITECTURE.md`.

Rationale:
- Aligns with Flask-first architecture and reduces implementation complexity.
- Makes route semantics and UI behavior easier to enforce in integration tests.
- Keeps V1 maintainable while preserving a clean migration path for Phase 2 UX abstraction.

---

## 3. Route and Screen Inventory

V1 defines 14 route contracts (`RT-01` to `RT-14`).

Route type split:
- Primary screen routes: 9
- Action/status routes: 5

Primary screen routes:
- `RT-01` Login View (`GET /login`)
- `RT-04` Preferences View (`GET /preferences`)
- `RT-05` Cluster List (`GET /clusters`)
- `RT-06` Cluster Detail (`GET /clusters/{cluster_id}`)
- `RT-09` Generated Article View (`GET /generated-articles/{article_id}`)
- `RT-10` Synthesis Audit View (`GET /generated-articles/{article_id}/audit`)
- `RT-11` Brief Composer (`GET /briefs/new`)
- `RT-13` Brief List (`GET /briefs`)
- `RT-14` Brief Detail (`GET /briefs/{brief_id}`)

Action/status routes:
- `RT-02` Login Action
- `RT-03` Logout Action
- `RT-07` Generation Request
- `RT-08` Generation Status
- `RT-12` Brief Create Action

---

## 4. Visual Direction (V1)

V1 UI should feel operational and editorial, not consumer-reader polished.

Style guidance:
- High-legibility typography with clear hierarchy.
- Dense but structured data presentation.
- Explicit status badges and operational states.
- Minimal decorative motion; motion should communicate system state transitions.

Suggested type pairing:
- UI/headings: `IBM Plex Sans` (fallback: sans-serif)
- Long-form generated article body: `Source Serif 4` (fallback: serif)

Suggested semantic color tokens:
- `--color-status-queued`
- `--color-status-running`
- `--color-status-success`
- `--color-status-failed`
- `--color-info-gap-thin`
- `--color-info-gap-moderate`
- `--color-info-gap-high-depth`

---

## 5. Application Layout Contract

### 4.1 Unauthenticated Layout
- Used only by `RT-01` login view.
- Single centered panel with:
  - Product title
  - Login form
  - Authentication error area

### 4.2 Authenticated App Shell
- Used by all authenticated screen routes.
- Shared regions:
  - Top bar: app title, signed-in user indicator, logout action.
  - Left navigation rail: `Clusters`, `Preferences`, `Briefs`.
  - Main content region: route-specific screen content.
- Optional right context panel on desktop for route-specific metadata:
  - Cluster detail source metadata
  - Article generation/audit quick links

### 4.3 Responsive Behavior
- Desktop breakpoint: three-region shell (top, left nav, main; optional right panel).
- Mobile/tablet: top bar + collapsible nav drawer; right panel content folds into main flow.
- Primary actions remain visible without horizontal scrolling.

---

## 6. Shared Component Contracts

### 5.1 Status Pill
Used for generation and job-like lifecycle displays.

Allowed values:
- `queued`
- `running`
- `success`
- `failed`

### 5.2 Information Gap Badge
Displayed on cluster list and cluster detail (`FR-013C`, `FR-013D`).

Allowed values:
- `Thin`
- `Moderate`
- `High Depth`

### 5.3 Source Visibility Marker
Cluster detail should visibly indicate when source filtering is active due to user preferences.

Required behavior:
- Hidden/filtered sources are not rendered as selectable source rows.
- Screen shows a short note that user preferences are applied.

### 5.4 Citation Link Element
Generated article citations and audit entries must reference the same source identity.

Required behavior:
- Citation label in article maps to an audit row.
- Audit row displays source URL and provenance status.

---

## 7. Route-Level UI Contracts

### RT-01 Login View
- Shows username/password input and submit action.
- On failed auth, shows inline error without route change.

### RT-02 Login Action
- On success, redirects to `RT-05` cluster list.
- On failure, returns to `RT-01` with error state.

### RT-03 Logout Action
- Ends session and redirects to `RT-01`.

### RT-04 Preferences View/Update
- Shows editable topic/source preference controls.
- Save action confirms persistence and reflects latest values.

### RT-05 Cluster List
- Displays clusters with:
  - Recency
  - Source count
  - Information Gap badge
- Supports sorting by recency and source count.
- Each row links to `RT-06`.
- Empty state: "No clusters available yet."

### RT-06 Cluster Detail
- Displays cluster-level metadata and source list for manual selection.
- User preference filtering is applied before rendering source rows.
- Selection UI supports one or more selected source articles.
- Primary action: "Generate Article" (calls `RT-07`).

### RT-07 Generation Request
- Request should return quickly and create async lifecycle record.
- UI transitions into processing state immediately after acceptance.

### RT-08 Generation Status
- Cluster detail and/or generation panel polls status until terminal state.
- Polling should stop on `success` or `failed`.
- Terminal actions:
  - On `success`: show link to `RT-09`.
  - On `failed`: show retry guidance and failure message.

### RT-09 Generated Article View
- Displays immutable article content:
  - Headline
  - Body
  - Summary bullet
  - "Sources Used" section
- Displays article status when applicable (for non-terminal transitions during load race).
- Provides link to `RT-10` audit view.

### RT-10 Synthesis Audit View
- Table/list of citations with fields:
  - Citation label
  - Source URL
  - Provenance status
  - Optional excerpt
- If excerpt unavailable, show explicit "source-linked, excerpt unavailable" label.

### RT-11 Brief Composer
- Displays selectable generated articles for current user.
- Enforces brief composition target (10-15 articles) at UX level.
- Create action posts to `RT-12`.

### RT-12 Brief Create Action
- Creates immutable brief snapshot and redirects to `RT-14`.
- Cross-user article selection attempts fail with user-scoped error response.

### RT-13 Brief List
- Lists briefs by date/time, newest first by default.
- Each entry links to `RT-14`.

### RT-14 Brief Detail
- Displays immutable brief snapshot contents as stored.
- No edit controls.

---

## 8. UX State Rules

### 7.1 Loading States
- Every screen route must render a loading state when data is pending.
- Loading copy should identify the data type ("Loading clusters...", "Loading article...").

### 7.2 Empty States
- Cluster list empty: no clusters available.
- Brief list empty: no briefs generated.
- Audit view empty: show explicit "No citation provenance records found."

### 7.3 Error States
- Use inline, actionable error messages.
- Avoid generic "Something went wrong" when a domain message is available.

### 7.4 Async Generation Timing
- Generation UI must use polling (`RT-08`) instead of holding one long request.
- UI must clearly show processing state throughout `queued` and `running`.

---

## 9. Security and Isolation Presentation

- All authenticated views are user-scoped.
- UI must not render controls or data for assets owned by other users.
- On authorization failure, show an access-denied response and hide object details.

---

## 10. Accessibility Baseline (V1)

- Keyboard-navigable controls for all primary actions.
- Visible focus indicators.
- Sufficient color contrast for status badges.
- Semantic heading structure for each screen.
- Form validation messages bound to relevant fields.

---

## 11. Testing Expectations for UI Contracts

- Route-linked tasks must include integration tests for:
  - Route response semantics
  - Key UI state transitions (loading, empty, error, success where applicable)
- Status polling tests should verify transition flow:
  - `queued` -> `running` -> terminal state
- Audit tests should cover:
  - excerpt present
  - excerpt unavailable label behavior
