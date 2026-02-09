# Bug Report

### Describe the bug
When generating test files, the blank line spacing between tests is not being added correctly. It looks like blank lines are only being inserted before the first test when there are suites above it, but subsequent tests are not getting proper spacing between them.

### Reproduction
Generate a test file with multiple tests in a suite:

```js
// Example structure
suite('My Suite', () => {
  test('first test', () => {
    // test code
  });
  test('second test', () => {
    // test code
  });
  test('third test', () => {
    // test code
  });
});
```

The generated output should have blank lines between each test for readability, but currently the tests are being output without proper spacing between them (except possibly before the first test in certain conditions).

### Expected behavior
Each test should be separated by a blank line in the generated output for better readability, regardless of whether there are suites above or what position the test is in.

### System Info
- Package: insomnia-testing
- Node version: latest

---
Repository: /testbed
