# Bug Report

### Describe the bug

When creating a new unit test suite, the `create()` function is now asynchronous but existing code is calling it without awaiting the result. This causes the function to return a Promise instead of the created test suite object, breaking functionality that depends on synchronously accessing the created suite.

### Reproduction

```js
// This used to work but now fails
const newSuite = unitTestSuite.create({
  parentId: 'wrk_123',
  name: 'My Test Suite'
});

// newSuite is now a Promise, not the actual suite object
console.log(newSuite.name); // undefined - trying to access property on Promise
```

### Expected behavior

The function should either:
1. Remain synchronous and return the created suite object directly, OR
2. If it needs to be async, all callers should be updated to await the result

Currently trying to access properties on the returned value fails because it's a Promise object instead of the actual UnitTestSuite.

### System Info
- Insomnia version: latest
- The issue appeared after recent changes to the unit-test-suite model

---
Repository: /testbed
