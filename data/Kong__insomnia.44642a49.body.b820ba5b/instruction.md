# Bug Report

### Describe the bug
When using `expect.not.to.have.body()` in test scripts, the assertion is not working as expected. It appears that the negation logic is being ignored, causing tests to pass when they should fail.

### Reproduction
```js
pm.test("Response should not contain specific text", function () {
    pm.expect(pm.response).to.not.have.body("error message");
});
```

Even when the response body contains "error message", the test passes instead of failing. The positive assertion `pm.expect(pm.response).to.have.body()` works fine, but the negated version doesn't behave correctly.

### Expected behavior
When using `.not.to.have.body()`, the assertion should fail if the response body contains the specified text, and pass if it doesn't contain it.

### Additional context
This seems to have started happening recently. The positive assertions work fine, but all the negated body assertions are broken. Other negated assertions like `.not.to.have.status()` and `.not.to.have.header()` still work correctly, so this appears to be specific to the body assertion.

---
Repository: /testbed
