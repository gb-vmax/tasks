# Bug Report

### Describe the bug
When making requests that return empty responses, I'm getting unexpected behavior with the response body handling. It seems like the application is trying to read from a file path even when there's no body content, which causes issues.

### Reproduction
```js
// Make a request that returns no body (e.g., 204 No Content)
const response = await sendRequest({
  method: 'DELETE',
  url: 'https://api.example.com/resource/123'
});

// Try to access the response body
const body = getBodyBuffer(response);
// Expected: empty buffer or null
// Actual: throws error or unexpected behavior
```

### Steps to reproduce:
1. Send a request that returns a 204 No Content or similar empty response
2. Try to access the response body using `getBodyBuffer()`
3. Application attempts to read from bodyPath even though there's no body

### Expected behavior
When a response has no body content, `getBodyBuffer()` should return an empty buffer without attempting to read from the file system. The function should check if there's actually a body before trying to access the bodyPath.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with APIs that return empty responses for successful operations (like DELETE requests returning 204).

---
Repository: /testbed
