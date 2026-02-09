# Bug Report

### Describe the bug

After a recent update, the plugin response context is returning an empty string for `getStatusMessage()` when the response has a status code but no explicit status message. Previously, it would return the standard HTTP status text (like "OK" for 200, "Not Found" for 404, etc.).

### Reproduction

```js
// In a plugin, when accessing response status message:
const response = {
  statusCode: 200,
  statusMessage: '' // or undefined
}

// This now returns empty string instead of "OK"
const message = context.response.getStatusMessage()
console.log(message) // Expected: "OK", Actual: ""
```

Another example:
```js
// 404 response without explicit statusMessage
const response = {
  statusCode: 404,
  statusMessage: null
}

const message = context.response.getStatusMessage()
console.log(message) // Expected: "Not Found", Actual: ""
```

### Expected behavior

When a response doesn't have an explicit `statusMessage` but has a valid `statusCode`, `getStatusMessage()` should fall back to the standard HTTP status text for that code (e.g., "OK" for 200, "Not Found" for 404, etc.).

This is particularly problematic for plugins that display response information to users, as they now show blank status messages instead of the standard HTTP text.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
