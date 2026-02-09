# Bug Report

### Describe the bug

When using `expect(response).to.not.have.body()` in test scripts, the assertion is not working as expected. The negation doesn't properly validate that the response body is absent or empty.

### Reproduction

```js
pm.test("Response should not have body", function () {
    // This assertion fails even when body is empty
    pm.expect(pm.response).to.not.have.body('');
});

pm.test("Response with null body", function () {
    // Unexpected behavior with null/undefined values
    pm.expect(pm.response).to.not.have.body(null);
});
```

### Expected behavior

The `to.not.have.body()` assertion should correctly validate when a response body is absent or doesn't match the expected value. Currently it seems to be treating the negation case the same as the positive case.

### System Info
- Insomnia SDK version: latest
- Environment: Test script execution

---
Repository: /testbed
