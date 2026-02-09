# Bug Report

### Describe the bug

The `getRequestId()` method in the plugin response context is returning unexpected values. Instead of returning the request ID string, it's now returning `true` or `undefined`.

### Reproduction

```js
// In a plugin script
const requestId = insomnia.response.getRequestId();
console.log(requestId);
// Expected: "req_123abc..." (the actual request ID)
// Actual: true or undefined
```

When trying to use the request ID for further operations (like looking up request details or building references), the plugin fails because it receives a boolean/undefined instead of the expected string value.

### Expected behavior

`getRequestId()` should return the parent request ID as a string (or empty string if not available), not a boolean value.

### Additional context

This is breaking plugins that rely on getting the request ID to perform operations like:
- Looking up related requests
- Building request chains
- Logging request metadata

The method used to work correctly and return the actual ID string.

---
Repository: /testbed
