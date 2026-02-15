# Data Model (Template)

Project: `<ProjectName>`
Doc Status: `template` | `draft` | `frozen`
Last Updated (UTC): `<YYYY-MM-DD>`

Rules:
- Store timestamps in UTC.
- Enforce multi-user isolation with `user_id` on user-facing entities.

## 1. Entities

| Entity | Primary Key | Owner (`user_id`?) | Mutable? | Retention | Notes |
|---|---|---|---|---|---|
| User | id | N/A | yes | retain | |
| TBD | TBD | TBD | TBD | TBD | |

## 2. Relationships

- TBD

## 3. Uniqueness and Deduplication

- Natural keys:
- Uniqueness constraints:

## 4. Lineage / Provenance

- What must be immutable:
- What audit/provenance records are required:

