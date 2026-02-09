# Bug Report

### Describe the bug

I'm experiencing an issue with the `to.not.have.jsonBody()` assertion in the Insomnia SDK. When I try to use this negative assertion to verify that a response body does NOT match a specific JSON object, it's not working as expected.

### Reproduction

```js
const response = {
  body: JSON.stringify({ status: 'success', data: 'test' })
}

// This assertion doesn't behave correctly
pm.expect(response).to.not.have.jsonBody({ status: 'error' })
```

The negative assertion seems to be checking the wrong thing. It appears to be passing the wrong parameters internally.

### Expected behavior

When using `to.not.have.jsonBody()`, it should properly verify that the response body does NOT contain the specified JSON object. The assertion should pass when the actual JSON body is different from the expected one, and fail when they match.

### System Info
- Insomnia SDK version: latest
- Using pre-request/test scripts

---
Repository: /testbed
