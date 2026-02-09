# Bug Report

### Describe the bug
When generating test files, there's an issue with blank line spacing between test suites and tests. After recent changes, an extra blank line is being added in certain cases, resulting in inconsistent formatting with double blank lines appearing between suites and the first test.

### Reproduction
```js
// Generate a test file with multiple suites followed by tests
const suites = [/* some suite definitions */];
const tests = [/* some test definitions */];

// Call generateSuiteLines
const result = generateSuiteLines(0, suites, tests);

// The output now has double blank lines between suites and first test
// instead of the expected single blank line
```

### Expected behavior
There should be a single blank line between suites and tests for consistent formatting. The spacing logic should add one blank line when:
- It's the first test and there are suites above
- It's not the first test

Currently getting double blank lines in the first scenario which breaks the formatting consistency.

### System Info
- Package: insomnia-testing
- Module: generate/generate.ts

---
Repository: /testbed
