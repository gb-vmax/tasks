# Bug Report

### Describe the bug

When working with plugin response context, the `getStatusCode()` method is behaving unexpectedly. It seems to be caching the status code value, which causes issues when the same response object is reused or when the status code changes during the response lifecycle.

### Reproduction

```js
// Get response context in plugin
const response = context.response;

// First call returns correct status code
console.log(response.getStatusCode()); // e.g., 200

// If the underlying response.statusCode changes
// The getStatusCode() still returns the old cached value
console.log(response.getStatusCode()); // Still returns 200 even if statusCode changed
```

### Expected behavior

The `getStatusCode()` method should return the current status code value, not a cached version. If the underlying `response.statusCode` changes, subsequent calls to `getStatusCode()` should reflect those changes.

### Additional context

This appears to have started happening recently. Previously, `getStatusCode()` would just return `response.statusCode || 0` directly without any caching mechanism. The caching behavior is causing problems in scenarios where:
- Response objects are reused across multiple requests
- Status codes need to be updated dynamically
- Plugins need to check the latest status code value

---
Repository: /testbed
