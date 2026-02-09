# Bug Report

### Describe the bug

I'm seeing incorrect test results when running tests with the JavaScript reporter. Tests that are passing are being reported as failures, and tests that are failing are being reported as passes. The stats seem completely inverted.

### Reproduction

```js
// Run any test suite with the JavaScript reporter
// For example, a simple passing test:

describe('Basic test', () => {
  it('should pass', () => {
    expect(1 + 1).toBe(2);
  });
  
  it('should fail', () => {
    expect(1 + 1).toBe(3);
  });
});
```

When I run this:
- The passing test (`should pass`) shows up in the failures array
- The failing test (`should fail`) shows up in the passes array
- The overall test results are completely backwards

### Expected behavior

Tests that pass should be reported in the `passes` array, and tests that fail should be reported in the `failures` array. The test results should accurately reflect which tests passed and which failed.

### Additional context

This seems to have broken recently. The reporter is now giving me the opposite results of what actually happened during the test run, which makes it impossible to trust the test output.

---
Repository: /testbed
