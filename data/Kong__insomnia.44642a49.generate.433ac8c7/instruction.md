# Bug Report

### Describe the bug
When generating test suites, the first test suite in the array is being skipped and not included in the generated output. Only test suites at index 1 and beyond are being processed.

### Reproduction
```js
const suites = [
  { name: 'First Suite', tests: [...] },
  { name: 'Second Suite', tests: [...] },
  { name: 'Third Suite', tests: [...] }
];

const generated = generate(suites);
// Only 'Second Suite' and 'Third Suite' are included in the output
// 'First Suite' is missing
```

### Expected behavior
All test suites passed to the `generate()` function should be included in the generated test output, including the first one at index 0.

### Additional context
This appears to have started happening recently. The first test suite is completely missing from the generated code, which breaks test coverage for any tests defined in that suite.

---
Repository: /testbed
