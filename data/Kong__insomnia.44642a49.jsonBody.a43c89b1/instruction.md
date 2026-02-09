# Bug Report

### Describe the bug
When using `expect(response).to.not.have.jsonBody()` in test assertions, the negation doesn't work as expected. The assertion always passes regardless of whether the response body matches the expected JSON or not.

### Reproduction
```js
// This should fail but passes
pm.test("Response should not have specific JSON body", function () {
    pm.expect(pm.response).to.not.have.jsonBody({
        status: "success",
        data: "test"
    });
});

// Even when the response body actually contains this exact JSON,
// the assertion still passes
```

### Expected behavior
When using `.not.have.jsonBody()`, the assertion should fail if the response body matches the provided JSON object, and pass if it doesn't match.

Currently it seems like the negation is being ignored or inverted somehow.

### System Info
- insomnia-sdk version: latest
- Using the response object's expect interface

---
Repository: /testbed
