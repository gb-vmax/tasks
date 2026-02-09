# Bug Report

### Describe the bug

When using `response.to.not.have.header()` in test scripts, the assertion doesn't work correctly. It seems like the negation is being ignored and the assertion always passes or behaves unexpectedly.

### Reproduction

```js
pm.test("Response should not have X-Custom-Header", function () {
    pm.response.to.not.have.header('X-Custom-Header');
});
```

Even when the response DOES contain the `X-Custom-Header`, the test still passes when it should fail.

### Expected behavior

When using `to.not.have.header()`, the assertion should fail if the header exists in the response, and pass if the header doesn't exist.

### Additional context

This seems to affect the `header` assertion specifically when used with negation. Other assertions like `status` and `body` with `to.not.have` appear to work fine.

---
Repository: /testbed
