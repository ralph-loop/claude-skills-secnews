# SecNews Legacy Cleanup - Remove gemini-cli References

## TL;DR

> **Quick Summary**: Remove all legacy `gemini-cli` references from test infrastructure and close stale GitHub issues created by obsolete tooling.
> 
> **Deliverables**:
> - Updated `tests/test_secnews_feeds.py` with new User-Agent
> - Updated `.github/workflows/secnews_tester.yml` with human-readable issue message
> - GitHub Issues #2 and #3 closed with explanation
> 
> **Estimated Effort**: Quick (< 30 minutes)
> **Parallel Execution**: YES - 2 waves
> **Critical Path**: Task 1/2 (parallel) → Task 3 → Task 4

---

## Context

### Original Request
Clean up legacy `gemini-cli` references from the SecNews project:
1. Change User-Agent in test file from `Gemini-CLI-Tester/1.0` to `SecNews-Tester/1.0`
2. Remove `@gemini-cli` mention from workflow issue body message
3. Close stale GitHub Issues #2 and #3

### Interview Summary
**Key Discussions**:
- User confirmed gemini-cli is legacy tooling that should be completely removed
- GitHub Issues #2 and #3 have empty URL lists (workflow parsing issue) and obsolete mentions
- New User-Agent should be `SecNews-Tester/1.0` to match project name

**Research Findings**:
- `tests/test_secnews_feeds.py:27`: `headers = {'User-Agent': 'Gemini-CLI-Tester/1.0'}`
- `.github/workflows/secnews_tester.yml:95`: `issue_body += "\n@gemini-cli please remediate these broken links."`
- Both issues are open and actionable

### Self-Review Gap Analysis
**Identified Gaps** (addressed in plan):
- What to replace @gemini-cli message with → Human-actionable message: "Please investigate and fix these broken feed URLs."
- Issue closure message needed → Will explain legacy tooling context

---

## Work Objectives

### Core Objective
Remove all traces of obsolete `gemini-cli` tooling from the SecNews test infrastructure and clean up stale issues it created.

### Concrete Deliverables
- `tests/test_secnews_feeds.py` - User-Agent updated
- `.github/workflows/secnews_tester.yml` - Issue message updated
- GitHub Issues #2 and #3 - Closed with explanation

### Definition of Done
- [ ] `pytest tests/test_secnews_feeds.py -v --collect-only` runs without errors
- [ ] No occurrences of `gemini` (case-insensitive) in test files or workflow
- [ ] GitHub Issues #2 and #3 are in closed state

### Must Have
- User-Agent changed to `SecNews-Tester/1.0`
- @gemini-cli reference removed from workflow
- Issues #2 and #3 closed

### Must NOT Have (Guardrails)
- Do NOT modify test logic or assertions
- Do NOT change workflow structure (jobs, triggers, steps)
- Do NOT modify feed URLs or `secnews_feeds.md`
- Do NOT create new issues or labels
- Do NOT change timeout values or other test parameters

---

## Verification Strategy (MANDATORY)

### Test Decision
- **Infrastructure exists**: YES (pytest + GitHub Actions)
- **User wants tests**: Manual verification (no new test code needed)
- **Framework**: pytest (existing)

### Manual Execution Verification

Each task includes specific verification commands that MUST be executed.

---

## Task Dependency Graph

| Task | Depends On | Reason |
|------|------------|--------|
| Task 1 | None | Independent file edit |
| Task 2 | None | Independent file edit |
| Task 3 | None | Can run in parallel (no file dependency) |
| Task 4 | Task 1, Task 2, Task 3 | Must verify ALL changes completed |

---

## Parallel Execution Graph

```
Wave 1 (Start immediately - all independent):
├── Task 1: Update User-Agent in test file
├── Task 2: Update issue message in workflow
└── Task 3: Close GitHub Issues #2 and #3

Wave 2 (After Wave 1 completes):
└── Task 4: Verify all changes

Critical Path: Any Task (1|2|3) → Task 4
Parallel Speedup: ~60% faster than sequential (3 tasks run simultaneously)
```

---

## TODOs

- [ ] 1. Update User-Agent in Test File

  **What to do**:
  - Edit `tests/test_secnews_feeds.py`
  - Line 27: Change `'User-Agent': 'Gemini-CLI-Tester/1.0'` to `'User-Agent': 'SecNews-Tester/1.0'`

  **Must NOT do**:
  - Do NOT change timeout value (keep 15)
  - Do NOT modify the try/except structure
  - Do NOT change any other headers

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-line change in one file, trivial complexity
  - **Skills**: [`git-master`]
    - `git-master`: Will create atomic commit for this change

  **Skills Evaluated but Omitted**:
  - `python-programmer`: Not needed - no logic changes, just string replacement
  - `frontend-ui-ux`: No frontend work
  - `typescript-programmer`: Python file, not TypeScript

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3)
  - **Blocks**: Task 4 (verification)
  - **Blocked By**: None (can start immediately)

  **References**:

  **Pattern References**:
  - `tests/test_secnews_feeds.py:22-32` - Full test function context showing where User-Agent is used

  **Acceptance Criteria**:

  - [ ] `grep -n "Gemini" tests/test_secnews_feeds.py` → No output (no matches)
  - [ ] `grep -n "SecNews-Tester" tests/test_secnews_feeds.py` → Shows line 27
  - [ ] `python -m py_compile tests/test_secnews_feeds.py` → Exit code 0 (valid Python syntax)

  **Commit**: YES
  - Message: `fix(tests): replace legacy Gemini User-Agent with SecNews-Tester`
  - Files: `tests/test_secnews_feeds.py`
  - Pre-commit: `python -m py_compile tests/test_secnews_feeds.py`

---

- [ ] 2. Update Issue Message in Workflow

  **What to do**:
  - Edit `.github/workflows/secnews_tester.yml`
  - Line 95: Change `issue_body += "\n@gemini-cli please remediate these broken links."` to `issue_body += "\n\nPlease investigate and fix these broken feed URLs."`

  **Must NOT do**:
  - Do NOT change the Python parsing logic
  - Do NOT modify job structure or triggers
  - Do NOT change issue title or labels
  - Do NOT remove the newline formatting

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single-line string change in YAML-embedded Python
  - **Skills**: [`git-master`]
    - `git-master`: Will create atomic commit for this change

  **Skills Evaluated but Omitted**:
  - `python-programmer`: Not needed - simple string replacement
  - `typescript-programmer`: Not TypeScript
  - `frontend-ui-ux`: No frontend work

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3)
  - **Blocks**: Task 4 (verification)
  - **Blocked By**: None (can start immediately)

  **References**:

  **Pattern References**:
  - `.github/workflows/secnews_tester.yml:65-103` - Full parse_failures step showing Python script context

  **Acceptance Criteria**:

  - [ ] `grep -in "gemini" .github/workflows/secnews_tester.yml` → No output (no matches)
  - [ ] `grep -n "Please investigate" .github/workflows/secnews_tester.yml` → Shows line 95
  - [ ] Workflow YAML is valid (no syntax errors)

  **YAML Validation**:
  - [ ] Using shell: `python -c "import yaml; yaml.safe_load(open('.github/workflows/secnews_tester.yml'))"`
  - [ ] Expected: Exit code 0, no output (valid YAML)

  **Commit**: YES
  - Message: `fix(ci): remove legacy gemini-cli reference from workflow issue message`
  - Files: `.github/workflows/secnews_tester.yml`
  - Pre-commit: `python -c "import yaml; yaml.safe_load(open('.github/workflows/secnews_tester.yml'))"`

---

- [ ] 3. Close GitHub Issues #2 and #3

  **What to do**:
  - Close Issue #2 with comment explaining closure
  - Close Issue #3 with comment explaining closure
  - Use `gh issue close` command with `--comment` flag

  **Closure Message**:
  ```
  Closing this issue as it was created by legacy automated tooling (gemini-cli) that has been removed from the project.
  
  This issue contains an empty URL list due to a workflow parsing issue at the time of creation. The workflow has been updated to produce actionable issues going forward.
  
  If there are actual broken feeds, a new issue will be created by the updated CI pipeline.
  ```

  **Must NOT do**:
  - Do NOT delete the issues (keep for audit trail)
  - Do NOT edit the issue body
  - Do NOT change labels or assignees

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Two simple CLI commands
  - **Skills**: [`git-master`]
    - `git-master`: Familiar with gh CLI and GitHub operations

  **Skills Evaluated but Omitted**:
  - `python-programmer`: No Python code
  - `frontend-ui-ux`: No UI work
  - `agent-browser`: CLI-based, no browser needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2)
  - **Blocks**: Task 4 (verification)
  - **Blocked By**: None (can start immediately)

  **References**:

  **Documentation References**:
  - GitHub CLI docs: `gh issue close --help`

  **Acceptance Criteria**:

  - [ ] `gh issue view 2 --json state -q '.state'` → `CLOSED`
  - [ ] `gh issue view 3 --json state -q '.state'` → `CLOSED`
  - [ ] Both issues have closure comment visible

  **Commit**: NO (no file changes)

---

- [ ] 4. Verify All Changes

  **What to do**:
  - Run comprehensive verification to ensure all changes are correct
  - Confirm no gemini references remain anywhere in test infrastructure
  - Verify pytest can still collect and run tests

  **Must NOT do**:
  - Do NOT make any changes in this task
  - Do NOT commit anything

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Verification commands only, no complex analysis
  - **Skills**: []
    - No specialized skills needed for running verification commands

  **Skills Evaluated but Omitted**:
  - `git-master`: No git operations in verification
  - `python-programmer`: Just running commands, not writing code

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2 (sequential after Wave 1)
  - **Blocks**: None (final task)
  - **Blocked By**: Tasks 1, 2, 3 (all must complete first)

  **References**:

  **Documentation References**:
  - pytest collection: `pytest --collect-only --help`

  **Acceptance Criteria**:

  **Global Gemini Check**:
  - [ ] `grep -rin "gemini" tests/ .github/workflows/` → No output (zero matches)

  **Test Collection**:
  - [ ] `pytest tests/test_secnews_feeds.py --collect-only` → Shows parametrized test cases, exit code 0

  **GitHub Issues**:
  - [ ] `gh issue list --state closed --search "Remediate Broken"` → Shows issues #2 and #3

  **Commit**: NO (verification only)

---

## Commit Strategy

| After Task | Message | Files | Verification |
|------------|---------|-------|--------------|
| Task 1 | `fix(tests): replace legacy Gemini User-Agent with SecNews-Tester` | `tests/test_secnews_feeds.py` | `python -m py_compile tests/test_secnews_feeds.py` |
| Task 2 | `fix(ci): remove legacy gemini-cli reference from workflow issue message` | `.github/workflows/secnews_tester.yml` | YAML valid |
| Task 3 | N/A (no file changes) | N/A | Issues closed |
| Task 4 | N/A (verification only) | N/A | All checks pass |

---

## Success Criteria

### Verification Commands
```bash
# No gemini references in test infrastructure
grep -rin "gemini" tests/ .github/workflows/
# Expected: No output (exit code 1 - no matches)

# Test file has correct User-Agent
grep "SecNews-Tester" tests/test_secnews_feeds.py
# Expected: headers = {'User-Agent': 'SecNews-Tester/1.0'}

# Workflow has correct message
grep "Please investigate" .github/workflows/secnews_tester.yml
# Expected: issue_body += "\n\nPlease investigate and fix these broken feed URLs."

# Issues are closed
gh issue view 2 --json state -q '.state'
gh issue view 3 --json state -q '.state'
# Expected: CLOSED (for both)

# Tests can still be collected
pytest tests/test_secnews_feeds.py --collect-only
# Expected: Shows 56+ parametrized tests, exit code 0
```

### Final Checklist
- [ ] All "Must Have" present (User-Agent changed, @gemini-cli removed, issues closed)
- [ ] All "Must NOT Have" absent (no test logic changes, no workflow structure changes)
- [ ] Zero occurrences of "gemini" in test infrastructure
- [ ] Test collection successful
