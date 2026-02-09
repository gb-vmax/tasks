# Bug Report

### Describe the bug

The test suite generation is adding extra blank lines in the output. When generating test files, there's an unexpected blank line appearing before the first test case that shouldn't be there.

### Reproduction

```js
const suites = [];
const tests = [
  { name: 'test1', assertions: [] },
  { name: 'test2', assertions: [] }
];

// Generate test suite
const output = generateSuiteLines(0, suites, tests);

// First test now has a blank line before it when it shouldn't
```

### Expected behavior

When there are no nested suites and we're outputting the first test (i === 0), there should not be a blank line added before it. Blank lines should only appear:
- Between tests (when i > 0)
- After outputting suites (when suites.length > 0)

Currently, a blank line is being added before the very first test even when there are no suites above it, which creates unnecessary whitespace at the beginning of the generated test file.

### System Info
- Package: insomnia-testing
- Node version: 18.x

---
Repository: /testbed
