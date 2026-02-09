# Bug Report

### Describe the bug

I'm experiencing a syntax error in the response expectations API. When trying to use the `to.not.have.jsonBody()` method, the code fails to execute properly. It looks like there's a malformed object structure in the response object definitions.

### Reproduction

```js
pm.test("Check response does not have specific JSON body", function () {
    pm.expect(pm.response).to.not.have.jsonBody({ key: "value" });
});
```

When running this, I get an error indicating that the response object structure is invalid.

### Expected behavior

The `to.not.have.jsonBody()` method should work correctly for negative assertions, allowing me to verify that a response does NOT contain a specific JSON body structure.

### Additional context

This seems to have broken recently. The positive assertion `to.have.jsonBody()` might be working, but the negative case with `to.not.have` is definitely failing. The error suggests there's a problem with how the object is being constructed in the expectations API.

---
Repository: /testbed
