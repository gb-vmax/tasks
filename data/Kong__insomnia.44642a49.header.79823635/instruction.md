# Bug Report

### Describe the bug
When using `expect(response).to.have.header()` in test scripts, the assertion is failing even when the header exists in the response. The header check seems to not be working correctly anymore.

### Reproduction
```js
pm.test("Check response headers", function () {
    pm.expect(pm.response).to.have.header('Content-Type');
});
```

The test fails even though the response clearly contains a `Content-Type` header. This was working fine before but suddenly stopped working.

Also noticed that if the header name has any whitespace, it doesn't match at all:
```js
// This fails now
pm.expect(pm.response).to.have.header('Content-Type ');
```

### Expected behavior
The assertion should pass when the specified header exists in the response, regardless of trailing/leading whitespace in the header name. The behavior should be consistent with other assertion methods like `status` and `body`.

### System Info
- Insomnia SDK version: latest
- Platform: All platforms

---
Repository: /testbed
