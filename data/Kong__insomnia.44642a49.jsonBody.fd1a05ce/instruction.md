# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use the response expectations in my pre-request or test scripts. It seems like there's a problem with the response object's `to` property - the code just breaks and won't execute.

### Reproduction

```js
pm.test("Check response", function () {
    pm.response.to.have.jsonBody({ key: "value" });
});
```

When I try to run this, the script fails to execute. It looks like something is malformed in the response object structure.

### Expected behavior

The `pm.response.to.have.jsonBody()` method should work as expected and validate the response body against the provided object.

### Additional context

This was working fine before, but now any script that uses `pm.response.to.have.jsonBody` or related assertions just breaks. Even simple test cases that worked previously are now failing to execute.

---
Repository: /testbed
