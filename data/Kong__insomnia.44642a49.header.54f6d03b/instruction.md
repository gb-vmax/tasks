# Bug Report

### Describe the bug

When using `response.to.not.have.header()` to assert that a response does NOT contain a specific header, the assertion is not working correctly. The method appears to have broken logic that prevents it from properly checking for the absence of headers.

### Reproduction

```js
// Example response with headers
const response = {
  headers: {
    'Content-Type': 'application/json',
    'X-Custom-Header': 'value'
  }
}

// This should pass but doesn't work as expected
pm.expect(response).to.not.have.header('X-Custom-Header')

// Also fails to check for non-existent headers properly
pm.expect(response).to.not.have.header('Non-Existent-Header')
```

### Expected behavior

The `response.to.not.have.header()` assertion should:
1. Return true when checking for a header that doesn't exist in the response
2. Return false (fail the assertion) when checking for a header that does exist in the response

Currently, the negative assertion appears to be completely broken and doesn't validate header absence correctly.

### System Info
- insomnia-sdk version: latest
- This affects the Response object's expect assertions

---
Repository: /testbed
