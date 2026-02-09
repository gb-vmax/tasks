# Bug Report

### Describe the bug
When calling `getStatusCode()` on a response object, I'm getting unexpected return values in certain scenarios. Instead of returning a numeric status code or 0 as a fallback, the method appears to be returning the entire response object when `statusCode` is not set.

### Reproduction
```js
// When response.statusCode is undefined or falsy
const response = {
  parentId: 'req_123',
  statusMessage: 'OK',
  // statusCode is not set
}

const statusCode = response.getStatusCode()
// Expected: 0
// Actual: returns the entire response object
```

### Expected behavior
The method should return a numeric status code. If `response.statusCode` is not available, it should return `0` as the default fallback value, not the response object itself.

### System Info
- Insomnia version: latest
- Using plugin context API

This is causing issues in my plugin where I'm trying to perform numeric comparisons on status codes and getting type errors instead.

---
Repository: /testbed
