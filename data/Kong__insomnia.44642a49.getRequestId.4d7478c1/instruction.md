# Bug Report

### Describe the bug

After a recent update, the plugin context's `getRequestId()` method is returning cached values across different responses. When processing multiple responses in sequence, the second and subsequent calls return the request ID from the first response instead of the actual parent ID for each response.

### Reproduction

```js
// First response
const response1 = {
  parentId: 'req_abc123',
  statusCode: 200
};
const context1 = createResponseContext(response1);
console.log(context1.getRequestId()); // Returns: 'req_abc123' ✓

// Second response with different parent
const response2 = {
  parentId: 'req_xyz789',
  statusCode: 200
};
const context2 = createResponseContext(response2);
console.log(context2.getRequestId()); // Returns: 'req_abc123' ✗ (should be 'req_xyz789')
```

### Expected behavior

Each response context should return its own `parentId` when `getRequestId()` is called. The method should not cache values across different response instances.

### Additional context

This appears to be affecting plugin scripts that process multiple responses, as they all receive the same request ID regardless of which response is being accessed. The caching seems to persist between different response objects.

---
Repository: /testbed
