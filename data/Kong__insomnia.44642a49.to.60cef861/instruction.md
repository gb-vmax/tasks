# Bug Report

### Describe the bug

The response object's assertion methods are not working properly. When trying to use `insomnia.response.to.have.status()`, `insomnia.response.to.have.header()`, or `insomnia.response.to.have.body()` in test scripts, these methods are no longer accessible and throw errors.

### Reproduction

```js
// In a test script
pm.test("Status code is 200", function () {
    insomnia.response.to.have.status(200);
});

pm.test("Response has header", function () {
    insomnia.response.to.have.header('Content-Type');
});

pm.test("Response body matches", function () {
    insomnia.response.to.have.body('expected body');
});
```

All of these assertions fail with errors indicating that the methods are undefined or cannot be called.

### Expected behavior

The `to.have` chain should work as before, allowing assertions on:
- Response status codes
- Response headers
- Response body content
- JSON body validation
- JSON schema validation

This was working fine in previous versions but seems to have broken recently.

### System Info
- Insomnia SDK version: latest
- Platform: macOS

---
Repository: /testbed
