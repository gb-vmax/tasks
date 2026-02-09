# Bug Report

### Describe the bug
After a recent update, the test file generator is producing output with inconsistent spacing between test cases. Some tests have double blank lines between them while others have single blank lines, making the generated test files look messy and inconsistent.

### Reproduction
When generating test suites with multiple test cases, the spacing between tests is no longer uniform. For example:

```js
// Generated output now looks like this:
describe('My Suite', () => {
  test('first test', () => {
    // ...
  });

  test('second test', () => {
    // ...
  });

  // Extra blank line appears here
  test('third test', () => {
    // ...
  });
});
```

Expected all tests to have the same single blank line separation like before, but now some tests randomly get double blank lines between them.

### Steps to reproduce
1. Create a test suite with multiple test cases
2. Generate the test file using the testing package
3. Observe inconsistent blank line spacing between different tests

### Expected behavior
All tests should be separated by a consistent single blank line, regardless of their names or order. The generated test files should have uniform formatting throughout.

### System Info
- Package: insomnia-testing
- The issue appears to be in the test generation logic

---
Repository: /testbed
