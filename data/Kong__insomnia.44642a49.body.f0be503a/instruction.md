# Bug Report

### Describe the bug

After a recent update, the response assertion methods seem to have broken syntax. When trying to use `response.to.not.have.body()` or other negation assertions, the code appears to be malformed and causes errors.

### Reproduction

```js
// Trying to assert that response does not contain certain text
pm.test("Response validation", function () {
    pm.response.to.not.have.body("error message");
});
```

The assertion methods are not functioning properly. It looks like there might be a syntax issue with how the negation chain is structured.

### Expected behavior

The `to.not.have.body()` assertion should work correctly to verify that the response body does not contain the specified string. Similarly, other negation assertions like `to.not.have.status()` and `to.not.have.header()` should function as expected.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
