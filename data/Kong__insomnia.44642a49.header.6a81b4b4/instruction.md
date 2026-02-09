# Bug Report

### Describe the bug

After a recent update, the response assertion API seems broken. When I try to use `expect(response).to.not.have.header()` in my test scripts, I'm getting syntax errors or the code just doesn't execute properly.

### Reproduction

```js
pm.test("Response should not contain auth header", function () {
    pm.expect(pm.response).to.not.have.header('Authorization');
});
```

The test script fails to parse or run. It looks like there might be an issue with how the negation assertions are structured in the SDK.

### Expected behavior

The `not.have.header()` assertion should work correctly to verify that a header is NOT present in the response. This was working fine in previous versions.

### Additional context

This affects all tests using negative header assertions. Positive assertions with `expect(response).to.have.header()` seem to work fine, it's only the `.not.have.header()` path that's broken.

---
Repository: /testbed
