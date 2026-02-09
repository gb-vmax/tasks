# Bug Report

### Describe the bug

After a recent update, the response body assertion appears to be broken. When trying to use `to.have.body()` in tests, I'm getting syntax errors or the assertion doesn't work as expected.

### Reproduction

```js
pm.test("Check response body", function() {
    pm.response.to.have.body("expected text");
});
```

The test fails to execute properly and throws an error. It seems like the body assertion method is malformed or incomplete.

### Expected behavior

The `to.have.body()` assertion should work correctly to validate response body content against a string value, just like it did in previous versions.

### System Info
- Insomnia SDK version: latest
- Node version: 18.x

---
Repository: /testbed
