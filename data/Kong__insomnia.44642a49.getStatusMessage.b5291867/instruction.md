# Bug Report

### Describe the bug

The `getStatusMessage()` method in the response plugin context is not working correctly after a recent change. When trying to access the status message from a response object, the method appears to be broken and likely returns undefined or causes an error.

### Reproduction

```js
// In a plugin that uses the response context
const response = context.response;
const statusMessage = response.getStatusMessage();
// This should return the status message but doesn't work as expected
```

Steps to reproduce:
1. Create a plugin that accesses the response context
2. Call `getStatusMessage()` on the response object
3. The method doesn't return the expected status message

### Expected behavior

The `getStatusMessage()` method should return the HTTP status message from the response (e.g., "OK", "Not Found", etc.). If the response has a custom status message, it should return that. Otherwise, it should fall back to standard HTTP status messages based on the status code.

### Additional context

This seems to have broken recently. The method was working fine before and now it's not accessible or not functioning properly. Looking at the code, there might be an issue with how the function is defined or scoped within the response context object.

---
Repository: /testbed
