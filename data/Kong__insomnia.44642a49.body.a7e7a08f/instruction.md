# Bug Report

### Describe the bug

The response body assertion methods are not working correctly after a recent update. When trying to use `to.have.body()` in test scripts, I'm getting syntax errors or unexpected behavior.

### Reproduction

```js
pm.test("Check response body", function () {
    pm.response.to.have.body("expected text");
});
```

When running this test, the script execution fails with parsing errors. It looks like there's a syntax issue in how the body assertion is being handled.

### Expected behavior

The `to.have.body()` assertion should work as before, allowing me to verify response body content without errors. The test should pass when the body matches the expected text and fail with a clear error message when it doesn't.

### Additional context

This was working fine in the previous version. The issue appeared after updating to the latest release. Other assertions like `to.have.status()` and `to.have.header()` still work correctly, it's only the body assertion that's affected.

---
Repository: /testbed
