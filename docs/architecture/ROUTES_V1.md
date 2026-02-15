# Routes (V1) (Template)

Project: `<ProjectName>`
Doc Status: `template` | `draft` | `frozen`
Last Updated (UTC): `<YYYY-MM-DD>`

Goal: define route behavior as a testable contract. Every route should map back to requirement IDs in `docs/product/REQUIREMENTS.md`.

## 1. Route Inventory

| RT ID | Method | Path | Auth Required | Purpose | Requirement Links | Notes |
|---|---|---|---|---|---|---|
| RT-001 | GET | `/health` | no | Service health check | N/A | |
| RT-002 | TBD | TBD | TBD | TBD | FR-001 | |

## 2. Contract Rules

- Success/empty/error shapes must be explicit per route.
- State-changing routes must define idempotency behavior.
- Async workflows must define status endpoint semantics.

