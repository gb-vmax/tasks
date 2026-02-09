# Bug Report

### Describe the bug

The `beforeEach` hook that clears the active request is being placed at the end of the generated test file instead of at the beginning. This causes the hook to run after all test suites are defined, which means tests that run earlier don't have the active request cleared properly before execution.

### Reproduction

When generating test suites, the output structure is incorrect:

```js
const { expect } = chai;

describe('My Test Suite', () => {
  it('should test something', () => {
    // test code here
  });
});

// beforeEach is placed AFTER the test suites
beforeEach(() => insomnia.clearActiveRequest());
```

### Expected behavior

The `beforeEach` hook should be placed at the top of the generated file, before any test suites are defined:

```js
const { expect } = chai;

// Clear active request before test starts (will be set inside test)
beforeEach(() => insomnia.clearActiveRequest());

describe('My Test Suite', () => {
  it('should test something', () => {
    // test code here
  });
});
```

This ensures that the active request is cleared before each test runs, regardless of test execution order.

### System Info
- Package: insomnia-testing

---
Repository: /testbed
