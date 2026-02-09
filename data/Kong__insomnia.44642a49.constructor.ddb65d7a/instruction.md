# Bug Report

### Describe the bug

The test reporter is showing incorrect test results - passing tests are being reported as failures, and failing tests are being reported as pending. The counts and classifications in the test results object don't match the actual test outcomes.

### Reproduction

When running tests with the JavaScriptReporter:

1. Create a test suite with some passing and some failing tests
2. Run the tests using the reporter
3. Check the `testResults` object

The results show:
- Tests that passed appear in the `failures` array
- Tests that failed appear in the `pending` array
- The `passes` array remains empty even when tests pass

### Expected behavior

Test results should be correctly categorized:
- Passing tests should appear in the `passes` array
- Failing tests should appear in the `failures` array  
- Pending tests should appear in the `pending` array

This makes it impossible to get accurate test reports and breaks any downstream tooling that relies on these results.

### System Info
- insomnia-testing version: latest
- Node version: 18.x

---
Repository: /testbed
