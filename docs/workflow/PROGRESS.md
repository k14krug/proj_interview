# PROGRESS (Template)

Purpose: append-only execution log for completed or attempted work.

Required fields are defined in `docs/harness/task-handshake.md`.

## Example Entry

### LOG-YYYYMMDD-01
- Timestamp (UTC): `YYYY-MM-DDTHH:MM:SSZ`
- Task ID: `PH-XX-YY` | `AH-XX`
- Type: `task` | `adhoc`
- Status: `success` | `blocked` | `partial`
- Accomplished:
  - TBD
- Files Changed:
  - TBD
- Commit Header(s):
  - TBD
- Tests Added/Updated:
  - TBD
- Test Results:
  - TBD
- Technical Debt / Known Gaps:
  - TBD
- Next Step:
  - TBD
- Blockers (if any):
  - TBD

### LOG-20260219-01
- Timestamp (UTC): `2026-02-19T19:19:34Z`
- Task ID: `AH-01`
- Type: `adhoc`
- Status: `success`
- Accomplished:
  - Augmented `/PHASE [XX]` instructions to require a cross-phase preflight consistency review in new conversations.
  - Added required checks for prior-phase outcomes in `PROGRESS.md`, future-phase dependency scanning, and explicit preflight question gating before task execution.
- Files Changed:
  - `docs/harness/commands.md`
  - `docs/workflow/PROGRESS.md`
- Commit Header(s):
  - `N/A` (non-task documentation update)
- Tests Added/Updated:
  - `N/A`
- Test Results:
  - `./scripts/validate_docs.sh` -> `PASS` (pre-change)
  - `./scripts/validate_docs.sh` -> `PASS` (post-change)
- Technical Debt / Known Gaps:
  - None noted; practical effectiveness depends on consistent detail quality in future `PROGRESS.md` entries.
- Next Step:
  - Use the updated `/PHASE` preflight process in the next phase-start conversation and tune wording based on observed ambiguities.
- Blockers (if any):
  - `None`
