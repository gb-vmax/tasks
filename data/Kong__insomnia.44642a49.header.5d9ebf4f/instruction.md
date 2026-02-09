# Bug Report

### Describe the bug

The `to.have.header()` assertion is not working properly after a recent update. When trying to check for response headers in test scripts, the assertion seems to be broken and doesn't behave as expected.

### Reproduction

```js
// This used to work but now fails
pm.test("Check header exists", function() {
    pm.response.to.have.header('Content-Type');
});

// Also having issues with header value checks
pm.test("Check header value", function() {
    pm.response.to.have.header('Content-Type', 'application/json');
});
```

### Expected behavior

The header assertions should work correctly to verify the presence and values of response headers. The test should pass when the header exists and has the expected value.

### System Info

- Insomnia SDK version: latest
- Testing response headers with the `pm.response` object

This appears to have started happening after the most recent changes. The header checking functionality seems to have regressed somehow.

---
Repository: /testbed
