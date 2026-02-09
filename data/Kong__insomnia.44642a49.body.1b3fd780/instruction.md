# Bug Report

### Describe the bug
There seems to be a syntax error in the response body assertion code. When trying to use `expect.to.have.body()` in test scripts, I'm getting unexpected errors about the response object structure.

### Reproduction
```js
pm.test("Check response body", function () {
    pm.expect(pm.response).to.have.body("expected text");
});
```

The test fails with a parsing error or unexpected behavior when checking the response body. It looks like there might be an issue with how the body validation is set up internally.

### Expected behavior
The `expect.to.have.body()` assertion should work correctly and validate the response body content without throwing syntax errors.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
