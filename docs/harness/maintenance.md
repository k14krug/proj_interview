# Harness Maintenance

Use this checklist to keep the harness lean and accurate.

## Monthly Maintenance Checklist
1. Run `./scripts/validate_docs.sh`.
2. Remove stale TODO tasks or mark blocked tasks with current blockers.
3. Verify authority links and file paths still resolve.
4. Prune duplicated or contradictory rules across harness docs.
5. Review `docs/workflow/PROGRESS.md` for recurring failure patterns and open follow-up tasks.

## Change Discipline
- Prefer small, focused edits.
- Update `Last Updated` and `Change Summary` in `AGENTS.md` for harness-structure changes.
- Record meaningful harness changes in `docs/workflow/PROGRESS.md`.
