# Bug Report

### Describe the bug

I'm experiencing an issue with the `to.not.have.body()` assertion in the Insomnia SDK. When I use it to verify that a response body does NOT contain a specific string, it's not working as expected. The assertion seems to be modifying the expected value in some way, causing incorrect validation behavior.

### Reproduction

```js
pm.test("Response should not contain specific text", function () {
    pm.response.to.not.have.body("error");
});
```

When the response body is `"error"`, this test passes when it should fail. It seems like the negation check is comparing against a modified version of the expected string instead of the original value.

### Expected behavior

The `to.not.have.body()` assertion should correctly validate that the response body does NOT contain the exact string provided. If the response body is `"error"` and I'm checking for `to.not.have.body("error")`, the assertion should fail.

### Additional context

This seems to have started recently. The positive assertion `to.have.body()` works fine, but the negated version `to.not.have.body()` is behaving unexpectedly.

---
Repository: /testbed
