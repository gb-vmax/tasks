# Bug Report

### Describe the bug

When using `pm.response.to.not.have.jsonBody()` in test scripts, the assertion behavior is inverted. Instead of checking that the response body does NOT match the expected JSON, it's actually checking that it DOES match.

### Reproduction

```js
pm.test("Response should not have specific JSON body", function () {
    // This test fails even though the response body matches the expected JSON
    // It should pass since we're using .not.have
    pm.response.to.not.have.jsonBody({
        status: "success",
        data: "test"
    });
});
```

When the actual response body is:
```json
{
    "status": "success",
    "data": "test"
}
```

The test should pass (since we're asserting it should NOT have this body and it does), but instead it behaves incorrectly.

### Expected behavior

`pm.response.to.not.have.jsonBody(obj)` should pass when the response body does NOT match the expected JSON object, and fail when it DOES match. Currently it seems to be doing the opposite.

### System Info
- Insomnia SDK version: latest
- Platform: All platforms

---
Repository: /testbed
