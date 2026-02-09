# Bug Report

### Describe the bug
When generating test suites, the last test suite in the array is not being included in the generated output. Only the first n-1 suites are processed, causing the final suite to be silently dropped.

### Reproduction
```js
const suites = [
  { name: 'Suite 1', tests: [...] },
  { name: 'Suite 2', tests: [...] },
  { name: 'Suite 3', tests: [...] }
];

const result = generate(suites);
// Only Suite 1 and Suite 2 are present in the output
// Suite 3 is missing
```

### Expected behavior
All test suites passed to the `generate()` function should be included in the generated output, including the last one in the array.

### System Info
- insomnia-testing version: latest
- Node version: 18.x

---
Repository: /testbed
