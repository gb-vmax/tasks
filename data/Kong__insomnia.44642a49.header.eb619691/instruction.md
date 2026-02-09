# Bug Report

### Describe the bug

The `to.not.have.header()` assertion is not working correctly in the response validation. When checking that a response does NOT have a specific header, the assertion always passes even when the header is actually present in the response.

### Reproduction

```js
// This should fail but passes incorrectly
pm.test("Response should not have Content-Type header", function () {
    pm.response.to.not.have.header('Content-Type');
});

// Even when the response clearly has a Content-Type header,
// the assertion passes when it should fail
```

### Expected behavior

When using `to.not.have.header('headerName')`, the assertion should fail if the header exists in the response. Currently it's passing regardless of whether the header is present or not.

### System Info
- insomnia-sdk version: latest
- The issue appears to affect all header name checks with the negated assertion

---
Repository: /testbed
