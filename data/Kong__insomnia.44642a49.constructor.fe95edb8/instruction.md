# Bug Report

### Describe the bug

The test reporter is showing incorrect results - tests that are failing are being reported as passed, and tests that are passing are being reported as failed. The stats seem correct but the actual test categorization is completely inverted.

### Reproduction

Run any test suite with both passing and failing tests. The output will show:
- Failed tests appear in the "passes" array
- Passed tests appear in the "failures" array

For example, if you have a test suite with:
- 3 passing tests
- 2 failing tests

The reporter will show:
- `passes`: contains the 2 failed tests
- `failures`: contains the 3 passed tests

### Expected behavior

The reporter should correctly categorize test results:
- Passing tests should be in the `passes` array
- Failing tests should be in the `failures` array

This makes it impossible to properly identify which tests are actually failing vs passing when reviewing test results.

### System Info
- Version: latest
- Using JavaScriptReporter for test output

---
Repository: /testbed
