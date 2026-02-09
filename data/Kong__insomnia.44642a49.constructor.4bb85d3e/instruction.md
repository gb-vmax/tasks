# Bug Report

### Describe the bug

After a recent update, the test reporter is not generating any test results. When running tests, the `testResults` object is undefined and no test output is produced. It seems like the reporter stopped working completely.

### Reproduction

```js
// Run any test suite with the JavaScriptReporter
const runner = new Mocha.Runner();
const reporter = new JavaScriptReporter(runner, {});

// Execute tests
runner.run();

// Expected: runner.testResults should contain test results
// Actual: runner.testResults is undefined
```

### Expected behavior

The reporter should collect and store test results in `runner.testResults` with the following structure:
- stats
- tests
- pending
- failures  
- passes

Currently nothing is being captured and the results object remains undefined after test execution completes.

### System Info
- Node version: 16.x
- Mocha version: latest

---
Repository: /testbed
