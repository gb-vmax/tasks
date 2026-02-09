# Bug Report

### Describe the bug

When using `response.to.not.have.body()` in test assertions, the validation is not working as expected. The assertion appears to be passing even when the response body contains the specified content.

### Reproduction

```js
// This assertion should fail but passes
pm.test("Response should not contain text", function () {
    pm.response.to.not.have.body("expected content");
});

// Even when the response body clearly contains "expected content",
// the test passes when it should fail
```

### Expected behavior

When using `.not.have.body()`, the assertion should fail if the response body contains the specified string. Currently it seems like the negation is not being respected properly.

### System Info
- insomnia-sdk version: latest
- Using pre-request/test scripts

---
Repository: /testbed
