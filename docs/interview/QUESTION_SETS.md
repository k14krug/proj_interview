# Question Sets

Use sets in order. Revisit any set when follow-up triggers are hit.

---

## Set 01: Product Intent and Outcomes

Goal: define what the product is, who it serves, and what success looks like.

Primary questions:
1. What exact problem are we solving, and for whom?
2. What user outcomes must exist in V1 to call it successful?
3. What outcomes are explicitly out of scope for V1?
4. What business or operational constraints are fixed from day one?
5. What deadline or rollout constraints drive scope decisions?

Follow-up triggers:
1. If user types are broad, ask for top 1-2 primary personas only.
2. If success is vague, ask for measurable criteria.
3. If scope is large, ask what can be deferred without breaking V1 value.

Exit criteria:
1. V1 in-scope list is explicit.
2. V1 out-of-scope list is explicit.
3. Success criteria are measurable.

---

## Set 02: Product Phasing and Boundaries

Goal: separate V1 from future phases so implementation does not drift.

Primary questions:
1. What belongs in Phase 1, Phase 2, and later?
2. What capabilities must be excluded from V1 code paths?
3. What future flexibility must V1 preserve?
4. Are there hard "do not build yet" rules?
5. What migration assumptions should V1 avoid?

Follow-up triggers:
1. If a feature is "maybe V1", force a phase assignment.
2. If future mode depends on V1 structure, ask for non-negotiable invariants.

Exit criteria:
1. Phase boundaries are explicit and testable.
2. Anti-scope rules exist to prevent premature implementation.

---

## Set 03: Users, Auth, and Isolation

Goal: define user model, ownership rules, and access boundaries.

Primary questions:
1. Who can authenticate, and how?
2. What entities are user-owned vs global/shared?
3. What are hard isolation rules between users/tenants?
4. What authorization failures should users see?
5. Are there role-based behaviors in V1?

Follow-up triggers:
1. If entities are user-scoped, ask where `user_id` must be enforced.
2. If shared objects exist, ask how user-specific filtering is applied.
3. If no roles exist now, ask if schema should still anticipate roles later.

Exit criteria:
1. Ownership matrix is complete.
2. Isolation behavior is defined for read and write paths.

---

## Set 04: Domain Objects and Data Lifecycle

Goal: define data entities, lineage, mutability, and retention.

Primary questions:
1. What are the core entities and relationships?
2. Which tables/objects are immutable vs mutable?
3. What deduplication keys and uniqueness guarantees are required?
4. What lineage must be preserved end to end?
5. What retention and purge rules apply?
6. What timestamp/timezone storage rules apply?

Follow-up triggers:
1. If immutable data can be edited, ask what fields are exceptions and why.
2. If purge is allowed, ask what references must block deletion.
3. If lineage is required, ask what join tables/provenance records are mandatory.

Exit criteria:
1. ER-level shape is stable.
2. Mutability and retention rules are explicit.
3. Lineage preservation rules are explicit.

---

## Set 05: Core Workflows and Background Execution

Goal: define primary workflows and safe background execution semantics.

Primary questions:
1. What are the top end-to-end workflows in V1?
2. Which steps are synchronous vs asynchronous?
3. What jobs run on schedules, and with what frequency?
4. What execution guarantee is required (at-most-once, at-least-once, exactly-once)?
5. How are duplicate job runs prevented?
6. What crash/restart recovery behavior is required?
7. What idempotency boundaries are required by job type?

Follow-up triggers:
1. If jobs run in web workers, ask whether single dedicated worker is required.
2. If job uniqueness is required, ask for claim-key model (for example slot ledger).
3. If retries exist, ask how side effects are made safe.

Exit criteria:
1. Workflow state transitions are defined.
2. Job execution semantics are explicit and operationally safe.

---

## Set 06: Route Contracts and API Semantics

Goal: define route-level behavior as a testable contract.

Primary questions:
1. What are all V1 routes and methods?
2. What does each route do and what does it never do?
3. What are success, empty, and error responses for each route?
4. Which routes are read views vs actions/status endpoints?
5. What route-level authorization behavior is required?

Follow-up triggers:
1. If a behavior exists without a route, add or remove one explicitly.
2. If a route changes state, ask for idempotency and validation behavior.
3. If async behavior exists, ask for status endpoint semantics.

Exit criteria:
1. Canonical route inventory is complete.
2. Every route maps to requirement IDs.

---

## Set 07: UI Contracts and Interaction States

Goal: define screen-level layout and interaction states tied to routes.

Primary questions:
1. What is the UI technology approach in V1?
2. What shared app shell regions are required?
3. What screen inventory exists for authenticated and unauthenticated flows?
4. What status states, badges, and labels are canonical?
5. What are required loading, empty, error, and success states per screen?
6. What responsive behavior is required for desktop vs mobile?
7. What accessibility baseline is mandatory in V1?

Follow-up triggers:
1. If route behavior is defined but UI state is not, ask for explicit UI contract.
2. If async flows exist, ask exactly how polling/render transitions work.
3. If visual style is vague, ask for clear direction and token set.

Exit criteria:
1. Route-to-screen mapping is complete.
2. Shared components and state rules are explicit.

---

## Set 08: AI/External Integration and Validation Rules

Goal: define boundaries and validation requirements for AI/provider calls.

Primary questions:
1. What external systems are used (AI, APIs, feeds, storage)?
2. What must be validated before accepting generated output?
3. What provenance/audit data must be stored?
4. What failure handling and retry rules are required?
5. What must never happen in route handlers vs services?

Follow-up triggers:
1. If AI output is accepted directly, ask what strict validation gates are required.
2. If citations/provenance are required, ask what minimum persistence is mandatory.
3. If external APIs fail, ask for user-visible and operational failure behavior.

Exit criteria:
1. Integration responsibilities are bounded.
2. Validation contract is explicit and testable.

---

## Set 09: Non-Functional Requirements and Operations

Goal: define platform, performance, reliability, and observability constraints.

Primary questions:
1. What environment constraints are fixed (OS, DB, host, runtime)?
2. What secrets/config rules are mandatory?
3. What reliability constraints must hold in production?
4. What logs/metrics/traces are required for operations?
5. What security/compliance requirements exist?

Follow-up triggers:
1. If deployment is self-hosted, ask for web and worker service boundaries.
2. If reliability claims are made, ask what exact mechanisms enforce them.
3. If observability is required, ask for table/log destinations and fields.

Exit criteria:
1. Ops constraints are concrete.
2. Production safety model is explicit.

---

## Set 10: Delivery Harness and Execution Governance

Goal: define how implementation work will be sequenced, validated, and logged.

Primary questions:
1. How should tasks be structured and identified?
2. What completion checklist governs task closure?
3. What testing policy applies to behavior and route changes?
4. What commit policy applies (branching, message format, commit trigger)?
5. What progress log fields are mandatory for handoff?

Follow-up triggers:
1. If tasks lack requirement/route links, ask for stricter template rules.
2. If test exceptions are allowed, ask where gaps are tracked.
3. If project uses agent orchestration, ask for slash-command behavior.

Exit criteria:
1. Work execution policy is defined and enforceable.
2. Templates exist for TODO and PROGRESS tracking.

---

## Cross-Set Reconciliation Questions

Run these at the end of each pass:

1. Which requirement has no route or data model support yet?
2. Which route has no requirement ID?
3. Which async workflow has no status model?
4. Which immutable object still has an edit path?
5. Which purge path can break lineage?
6. Which UI contract has no test expectation?
7. Which open question blocks V1 start?
