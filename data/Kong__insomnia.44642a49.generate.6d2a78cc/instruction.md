# Bug Report

### Describe the bug

After a recent update, test suites are not being generated correctly. The first test suite in the array is being completely skipped during generation, which means any tests defined in the first suite never get executed.

### Reproduction

```js
const suites = [
  {
    name: 'First Suite',
    tests: [
      { name: 'Test 1', /* ... */ },
      { name: 'Test 2', /* ... */ }
    ]
  },
  {
    name: 'Second Suite',
    tests: [
      { name: 'Test 3', /* ... */ }
    ]
  }
];

const output = generate(suites);
// Output only contains "Second Suite" and its tests
// "First Suite" and its tests are missing
```

### Expected behavior

All test suites should be included in the generated output, including the first one. The generated test file should contain all suites with their respective tests.

### Additional context

This appears to have started happening recently. Previously all test suites were being generated correctly. Now only suites after the first one are included in the output.

---
Repository: /testbed
