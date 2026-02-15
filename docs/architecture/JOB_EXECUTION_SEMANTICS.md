# Job Execution Semantics (Template)

Project: `<ProjectName>`
Doc Status: `template` | `draft` | `frozen`
Last Updated (UTC): `<YYYY-MM-DD>`

Goal: define safe background execution semantics that prevent duplicates, support recovery, and are testable.

## 1. Job Types

| Job | Trigger | Frequency | Concurrency Policy | Guarantee | Idempotency Boundary |
|---|---|---|---|---|---|
| TBD | schedule | TBD | TBD | at-least-once | TBD |

## 2. Overlap Prevention (Claim Model)

Define how a worker claims work so duplicates are prevented:
- Claim key:
- Lock/lease duration:
- Renewal policy:
- What happens on crash:

## 3. Retries and Side Effects

- Retry policy:
- Safe side effects:
- Non-idempotent side effects (must be isolated/guarded):

## 4. Startup Recovery

- How stale “running” jobs are handled:
- How partial work is reconciled:

## 5. Observability

- Required log fields:
- Required metrics:

