# Bug Report

### Describe the bug

I'm experiencing an issue with the `to.not.have.body()` assertion in the Insomnia SDK. When checking that a response does NOT have a specific body content, the assertion is behaving unexpectedly - it seems to be trimming whitespace and possibly inverting the logic.

### Reproduction

```js
// This should pass but fails
pm.expect(response).to.not.have.body("test content");

// Even when the response body is "test content" (exact match),
// the assertion behaves incorrectly
```

The problem appears to be specific to the negative assertion (`to.not.have.body()`). The positive assertion (`to.have.body()`) works as expected.

### Expected behavior

When using `to.not.have.body(expected)`, the assertion should:
1. Pass when the response body does NOT match the expected string
2. Fail when the response body DOES match the expected string
3. Not modify the expected value (like trimming whitespace)

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
