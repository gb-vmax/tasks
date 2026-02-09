# Bug Report

### Describe the bug

When using `expect.to.not.have.body()` in test assertions, the expectation is not working correctly. The assertion passes even when the response body matches the provided value, which is the opposite of what should happen with a negated expectation.

### Reproduction

```js
// This should fail but passes
pm.test("Response should not contain body", function () {
    pm.response.to.not.have.body("expected text");
});

// Even when the response body is exactly "expected text",
// the negated assertion incorrectly passes
```

### Expected behavior

When using `to.not.have.body()`, the assertion should fail if the response body matches the expected value. Currently it seems like the negation is not being respected.

### System Info
- insomnia-sdk version: latest
- Platform: Multiple

---
Repository: /testbed
