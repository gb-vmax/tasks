# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to use the response assertions in my pre-request/test scripts. The code won't execute and throws an error about duplicate object keys.

### Reproduction

```js
pm.test("Check response", function() {
  pm.response.to.not.have.body("error");
});
```

When I try to run any test that uses `pm.response.to.not.have.body()`, the script fails to parse. It seems like there's a duplicate property definition causing a syntax error in the response object.

### Expected behavior

The `body` assertion should work normally without any parsing errors. Tests should be able to check response bodies using the `have.body()` and `not.have.body()` methods.

### System Info
- Insomnia SDK version: latest
- The issue appeared after the most recent update

---
Repository: /testbed
