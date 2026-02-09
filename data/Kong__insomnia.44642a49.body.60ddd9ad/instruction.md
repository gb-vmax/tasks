# Bug Report

### Describe the bug

When using `response.to.not.have.body()` in test assertions, the negation doesn't work correctly. The assertion always passes regardless of whether the body matches or not, making it impossible to verify that a response does NOT contain a specific body content.

### Reproduction

```js
// This should fail but passes incorrectly
pm.test('Response should not have specific body', function() {
  pm.response.to.not.have.body('expected content');
});

// Even when the response body is exactly 'expected content',
// the test still passes when it should fail
```

### Expected behavior

When using `.not.have.body()`, the assertion should fail if the response body matches the expected content, and pass if it doesn't match. Currently it seems to always pass.

### System Info
- insomnia-sdk version: latest
- Platform: All

---
Repository: /testbed
