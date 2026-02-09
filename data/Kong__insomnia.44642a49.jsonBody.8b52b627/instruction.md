# Bug Report

### Describe the bug

When using `pm.expect(response).to.not.have.jsonBody()` in test scripts, the assertion behaves incorrectly. Instead of checking that the response body does NOT match the expected JSON, it appears to be checking the opposite condition.

### Reproduction

```js
// Test script
pm.test("Response should not have specific JSON body", function () {
    const response = pm.response.json();
    
    // This should pass when the body is different, but fails
    pm.expect(pm.response).to.not.have.jsonBody({
        status: "success",
        data: "test"
    });
});
```

When the response body actually contains `{"status": "success", "data": "test"}`, the test passes when it should fail. Conversely, when the body is different, the test fails when it should pass.

### Expected behavior

The `.not.have.jsonBody()` assertion should pass when the response body does NOT match the expected JSON object, and fail when it does match.

### System Info
- Insomnia SDK version: latest
- The issue appears to be specific to the `jsonBody` assertion with the `.not` negation

---
Repository: /testbed
