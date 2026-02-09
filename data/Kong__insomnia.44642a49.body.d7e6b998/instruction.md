# Bug Report

### Describe the bug

I'm encountering a syntax error when using the `expect().to.have.body()` assertion in my pre-request and test scripts. The response validation seems to be broken after a recent update.

### Reproduction

```js
pm.test("Check response body", function () {
    pm.expect(pm.response).to.have.body("expected text");
});
```

When running this script, I get an error and the test fails to execute properly. It seems like there's a problem with how the body assertion is being parsed or structured.

### Expected behavior

The `expect().to.have.body()` assertion should work correctly when checking response bodies, whether using:
- Simple string matching
- Regular expressions
- Options objects with different matching modes

### Additional context

This was working fine before, but now any script that uses `to.have.body()` throws an error. The issue appears to affect all body assertion variants including string, regex, and object-based matching.

System: Insomnia SDK latest version

---
Repository: /testbed
