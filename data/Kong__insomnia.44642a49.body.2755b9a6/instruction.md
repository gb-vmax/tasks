# Bug Report

### Describe the bug
When using `expect(response).to.have.body()` in test scripts, I'm getting a syntax error. It looks like there's an issue with the response assertion methods - the code seems malformed and the `body` assertion is not working as expected.

### Reproduction
```js
pm.test("Response body check", function () {
    pm.expect(pm.response).to.have.body("expected text");
});
```

This throws an error when trying to execute the test script. The same issue occurs when trying to use the body assertion with any parameters.

### Expected behavior
The `expect(response).to.have.body()` assertion should work correctly to verify response body content, similar to how `status` and `header` assertions work.

### System Info
- Insomnia SDK version: latest
- Platform: All platforms

---
Repository: /testbed
