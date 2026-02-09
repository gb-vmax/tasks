# Bug Report

### Describe the bug
When generating test suites, the first test suite in the array is being skipped and not included in the generated output. Only test suites from index 1 onwards are being processed.

### Reproduction
```js
const suites = [
  {
    name: 'First Suite',
    tests: [/* ... */]
  },
  {
    name: 'Second Suite', 
    tests: [/* ... */]
  },
  {
    name: 'Third Suite',
    tests: [/* ... */]
  }
];

const result = generate(suites);
// Only 'Second Suite' and 'Third Suite' appear in the output
// 'First Suite' is missing
```

### Expected behavior
All test suites passed to the `generate()` function should be included in the generated test output, including the first one at index 0.

### Additional context
This seems to have started happening recently. Previously all suites were being generated correctly. When I pass an array of 3 test suites, only 2 of them show up in the final generated code.

---
Repository: /testbed
