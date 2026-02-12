#!/usr/bin/env bash
set -euo pipefail

errors=0

fail() {
  echo "ERROR: $1" >&2
  errors=$((errors + 1))
}

require_file() {
  local path="$1"
  if [[ ! -f "$path" ]]; then
    fail "Missing required file: $path"
  fi
}

require_file "AGENTS.md"
require_file "docs/product/REQUIREMENTS.md"
require_file "docs/architecture/ARCHITECTURE.md"
require_file "docs/architecture/ROUTES_V1.md"
require_file "docs/architecture/UI_V1.md"
require_file "docs/architecture/DATA_MODEL.md"
require_file "docs/architecture/JOB_EXECUTION_SEMANTICS.md"
require_file "docs/workflow/TODO.md"
require_file "docs/workflow/PROGRESS.md"

todo_path="docs/workflow/TODO.md"

if ! rg -q '^## Execution Phase [0-9]{2}$' "$todo_path"; then
  fail "TODO must contain at least one '## Execution Phase XX' section."
fi

if ! rg -q '^### PH-[0-9]{2}-[0-9]{2} \[[ x/!]\] .+$' "$todo_path"; then
  fail "TODO must contain at least one task header in '### PH-XX-YY [ ] Title' format."
fi

task_validation_output="$(awk '
BEGIN {
  in_task = 0
  task = ""
  req = 0
  route = 0
  errs = 0
}
function flush_task() {
  if (in_task == 1) {
    if (req == 0) {
      printf("Task %s is missing Requirement Links\\n", task)
      errs++
    }
    if (route == 0) {
      printf("Task %s is missing Route Links\\n", task)
      errs++
    }
  }
}
/^### PH-[0-9][0-9]-[0-9][0-9] \\[[ x/!]\\] / {
  flush_task()
  in_task = 1
  task = $2
  req = 0
  route = 0
  next
}
in_task == 1 && /^- Requirement Links:/ {
  req = 1
  next
}
in_task == 1 && /^- Route Links:/ {
  route = 1
  next
}
END {
  flush_task()
  if (errs > 0) {
    exit 1
  }
}
' "$todo_path" 2>/dev/null)" || true

if [[ -n "$task_validation_output" ]]; then
  while IFS= read -r line; do
    [[ -n "$line" ]] && fail "$line"
  done <<< "$task_validation_output"
fi

if (( errors > 0 )); then
  echo "validate_docs: FAIL ($errors issue(s))" >&2
  exit 1
fi

echo "validate_docs: PASS"
