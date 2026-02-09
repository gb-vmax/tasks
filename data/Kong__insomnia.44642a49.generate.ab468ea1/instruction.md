# Bug Report

### Describe the bug

When generating test suites, the first suite in the array is being skipped and not included in the generated output. Only test suites starting from index 1 onwards are being processed.

### Reproduction

```js
const suites = [
  { name: 'First Suite', tests: [...] },
  { name: 'Second Suite', tests: [...] },
  { name: 'Third Suite', tests: [...] }
];

const result = generate(suites);
// Only 'Second Suite' and 'Third Suite' appear in the output
// 'First Suite' is missing
```

### Expected behavior

All test suites in the array should be included in the generated output, including the first one at index 0.

### System Info
- insomnia-testing version: latest
- Node version: 18.x

---
Repository: /testbed
