# Bug Report

### Describe the bug
When using `pm.response.to.not.have.jsonBody()` in test scripts, the negation doesn't work correctly. The test always passes regardless of whether the JSON body matches or not.

### Reproduction
```js
pm.test("Response body should not match", function () {
    pm.response.to.not.have.jsonBody({
        "key": "value"
    });
});
```

Even when the response body is exactly `{"key": "value"}`, the test passes when it should fail.

### Expected behavior
When using `.not.have.jsonBody()`, the test should fail if the response body matches the expected JSON object, and pass if it doesn't match.

### Additional context
The positive assertion `pm.response.to.have.jsonBody()` works as expected - it's only the negated version that seems broken.

---
Repository: /testbed
