# Architecture (Template)

Project: `<ProjectName>`
Doc Status: `template` | `draft` | `frozen`
Last Updated (UTC): `<YYYY-MM-DD>`

## 1. System Overview

- One-paragraph summary:
- Primary actors (users/services):
- Primary outputs:

## 2. Core Principles and No-Go Rules

- Principle 1:
- Principle 2:
- No-go rule 1:
- No-go rule 2:

## 3. Components and Responsibilities

Describe the major components (web app, worker, scheduler, DB, external integrations) and what each owns.

| Component | Responsibility | Owns Data | Notes |
|---|---|---|---|
| Web | TBD | TBD | |
| Worker | TBD | TBD | |

## 4. Execution Model

- Request/response paths:
- Background execution paths (if any):
- Concurrency model:

## 5. External Integrations

| Integration | Purpose | Data In/Out | Failure Handling |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

## 6. Security and Isolation

- Authentication approach:
- Authorization approach:
- Multi-user isolation rules (`user_id` enforcement points):

## 7. Observability and Operations

- Logs:
- Metrics:
- Alerts:

## 8. Testing Strategy

- Unit:
- Integration:
- E2E (if any):

