# Bug Report

### Describe the bug

I'm noticing an issue with the test generation output formatting. When generating test suites, there's an extra blank line being added before the first test that shouldn't be there. This only happens when there are nested suites but no tests have been outputted yet.

### Reproduction

```js
const suites = [
  // some nested suite structure
];
const tests = [
  { name: 'first test', /* ... */ },
  { name: 'second test', /* ... */ }
];

// Generate test output
const output = generateSuiteLines(suites, tests);
```

When `suites.length > 0` and we're on the first test (`i === 0`), an unwanted blank line gets inserted before the first test case.

### Expected behavior

The first test should not have a preceding blank line, even when there are suites above it. Blank lines should only be added between tests (when `i !== 0`), not before the very first one.

### Current output:
```
describe('Suite', () => {

  test('first test', () => {
    // ...
  });
  
  test('second test', () => {
    // ...
  });
});
```

### Expected output:
```
describe('Suite', () => {
  test('first test', () => {
    // ...
  });
  
  test('second test', () => {
    // ...
  });
});
```

This is causing formatting inconsistencies in the generated test files.

---
Repository: /testbed
