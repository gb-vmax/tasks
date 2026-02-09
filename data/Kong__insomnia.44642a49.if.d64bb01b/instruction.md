# Bug Report

### Describe the bug

After a recent update, error responses are no longer being returned properly from the SDK. When a request fails (network error, timeout, etc.), the response object is now `undefined` instead of containing error information.

This is breaking our error handling logic since we were expecting to be able to access error details from the response object.

### Reproduction

```js
const response = await insomnia.send(request);

// response is now undefined when an error occurs
// Previously we could access error information here
if (!response) {
  // We have no way to know what went wrong
  console.log('Request failed but no error details available');
}
```

### Expected behavior

When a request fails, the SDK should still return a response object that contains error information (error message, error type, elapsed time, etc.) so that scripts can properly handle different error scenarios.

For example, we should be able to differentiate between:
- Network timeouts
- Connection refused errors  
- DNS resolution failures
- SSL/TLS errors

Currently all errors just result in `undefined` being returned.

### System Info
- insomnia-sdk version: latest
- Platform: macOS

---
Repository: /testbed
