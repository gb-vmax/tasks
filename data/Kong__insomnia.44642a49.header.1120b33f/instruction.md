# Bug Report

### Describe the bug

When using `pm.expect(response).to.have.header()` in test scripts, the header name matching is not working correctly. It seems like the header name is being converted to lowercase and the comparison logic has changed, causing tests that previously passed to now fail.

### Reproduction

```js
pm.test("Check Content-Type header", function () {
    pm.expect(pm.response).to.have.header('Content-Type');
});

pm.test("Check custom header", function () {
    pm.expect(pm.response).to.have.header('X-Custom-Header');
});
```

When the response contains headers with mixed case (e.g., `Content-Type`, `X-Custom-Header`), the test fails even though the headers are present in the response.

### Expected behavior

The header check should be case-insensitive and match headers regardless of their casing. If a response contains a `Content-Type` header, then `pm.expect(pm.response).to.have.header('Content-Type')` should pass. Similarly, `pm.expect(pm.response).to.have.header('content-type')` should also pass.

### System Info

- Insomnia SDK version: latest
- Platform: All platforms

---
Repository: /testbed
