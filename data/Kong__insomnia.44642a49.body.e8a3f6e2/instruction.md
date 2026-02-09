# Bug Report

### Describe the bug
After a recent update, the response body assertion methods are not working correctly. When trying to use `to.have.body()` or `to.not.have.body()` in test scripts, I'm getting unexpected errors or the assertions are failing even when the body content should match.

### Reproduction
```js
pm.test("Response body check", function() {
    pm.response.to.have.body("expected text");
});
```

When running this test, the assertion doesn't behave as expected. It seems like the body comparison logic might have been affected by recent changes.

### Expected behavior
The `to.have.body()` and `to.not.have.body()` assertions should work correctly for:
- String matching
- Substring matching with `{ containing: "text" }`
- RegExp pattern matching

All of these should properly validate the response body content and throw appropriate errors when assertions fail.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
