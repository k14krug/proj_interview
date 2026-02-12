# Document Mapping

Use this matrix to convert interview answers into the final documentation set.

## 1. Product Docs

### `docs/product/REQUIREMENTS.md`

Source sets:
1. Set 01
2. Set 02
3. Set 05
4. Set 06
5. Set 08
6. Set 09

Required outputs:
1. Functional requirements with IDs.
2. Non-functional requirements with IDs.
3. Explicit V1 scope and out-of-scope.
4. Success criteria and acceptance rules.

### `docs/product/PRODUCT_PHASES.md`

Source sets:
1. Set 01
2. Set 02

Required outputs:
1. Phase descriptions.
2. V1 exclusion guardrails.
3. Transition principle to later phases.

## 2. Architecture Docs

### `docs/architecture/ARCHITECTURE.md`

Source sets:
1. Set 03
2. Set 05
3. Set 08
4. Set 09

Required outputs:
1. System overview and core stack.
2. service boundaries and execution model.
3. architectural principles and no-go rules.
4. testing and deployment constraints.

### `docs/architecture/ROUTES_V1.md`

Source sets:
1. Set 06

Required outputs:
1. route inventory with IDs.
2. method/path/purpose semantics.
3. requirement links per route.

### `docs/architecture/UI_V1.md`

Source sets:
1. Set 07
2. Set 06

Required outputs:
1. layout and shell contract.
2. route-level UI behavior.
3. loading/empty/error/success states.
4. accessibility baseline.

### `docs/architecture/DATA_MODEL.md`

Source sets:
1. Set 03
2. Set 04
3. Set 08

Required outputs:
1. entities, keys, relationships.
2. mutability and retention rules.
3. lineage/provenance storage rules.

### `docs/architecture/JOB_EXECUTION_SEMANTICS.md`

Source sets:
1. Set 05
2. Set 09

Required outputs:
1. scheduler execution guarantees.
2. slot-claim and overlap prevention model.
3. crash/restart recovery and idempotency boundaries.

## 3. Harness and Workflow Docs

### `AGENTS.md`

Source sets:
1. Set 10
2. Set 02
3. Set 09

Required outputs:
1. canonical doc authority map.
2. command entry points.
3. invariants and validation protocol.

### `docs/harness/*.md`

Source sets:
1. Set 10

Required outputs:
1. command execution rules.
2. task handshake and completion checklist.
3. testing and commit policy.

### `docs/workflow/TODO.md` and `docs/workflow/PROGRESS.md`

Source sets:
1. Set 10
2. Set 01
3. Set 06

Required outputs:
1. phased task plan with requirement links and route links.
2. progress log template and concrete log entries.

## 4. Pre-Draft Completeness Checklist

Before drafting docs, verify:

1. Every critical requirement has an owner and status `decided`.
2. All route-affecting requirements map to at least one route.
3. All route contracts map to UI behaviors and tests.
4. Async workflows include explicit status transitions.
5. Data retention rules cannot violate immutable lineage.
6. Open questions are explicitly deferred with target phase/date.
