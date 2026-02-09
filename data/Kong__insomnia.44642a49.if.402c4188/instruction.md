# Bug Report

### Describe the bug

After a recent update, the SDK is not handling error responses properly. When a request fails (timeout, connection error, DNS issues, etc.), the response object is now `undefined` instead of returning an error response that can be inspected.

This breaks error handling in scripts since there's no way to programmatically check what went wrong or handle different error types differently.

### Reproduction

```js
const response = await insomnia.send(request);

// response is undefined when an error occurs
if (!response) {
  // Can't determine what type of error occurred
  // Can't access error details
  // Can't log or handle specific error types
}
```

### Expected behavior

The SDK should return a response object even when errors occur, so that scripts can:
- Check the error type (timeout, connection, DNS, SSL, etc.)
- Access error messages
- Implement custom error handling logic
- Log error details for debugging

Previously this worked fine but now error responses just return `undefined` making it impossible to handle errors gracefully in pre-request and test scripts.

### System Info
- Insomnia SDK version: latest
- Platform: All

---
Repository: /testbed
