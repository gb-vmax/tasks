# Bug Report

### Describe the bug

When using `response.to.not.have.body()` in test assertions, it's not working as expected. The assertion seems to be checking for an empty string match instead of verifying that the response body is absent or empty.

### Reproduction

```js
pm.test("Response should not have body", function () {
    pm.response.to.not.have.body();
});
```

When the response actually contains a body, the test still passes when it should fail. It seems like the negation isn't being applied correctly.

### Expected behavior

`response.to.not.have.body()` should fail when the response contains any body content, and pass only when the body is truly empty or absent.

### Additional context

This appears to affect the negative assertion path specifically - `response.to.have.body()` works fine, but the `.not.have.body()` variant doesn't behave correctly.

---
Repository: /testbed
