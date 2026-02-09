# Bug Report

### Describe the bug

The `getStatusMessage()` method in the response plugin context is returning incorrect values. When a response has an explicit status message set, it's being ignored and a default HTTP status message is returned instead based on the status code.

### Reproduction

```js
// Create a response with a custom status message
const response = {
  statusCode: 200,
  statusMessage: 'Custom Success Message'
};

// Initialize the plugin context
const context = init(response);

// This returns 'OK' instead of 'Custom Success Message'
console.log(context.getStatusMessage());
// Expected: 'Custom Success Message'
// Actual: 'OK'
```

### Expected behavior

When a response object has a `statusMessage` property set, `getStatusMessage()` should return that custom message. The fallback to standard HTTP status messages should only happen when `statusMessage` is not provided.

### Additional context

This appears to affect custom responses where servers send non-standard status messages. The method should prioritize the actual status message from the response over the generated default messages.

---
Repository: /testbed
