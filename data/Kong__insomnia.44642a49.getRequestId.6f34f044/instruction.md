# Bug Report

### Describe the bug

The `getRequestId()` method in the response context is returning incorrect values. It appears to be returning `response.requestId` instead of `response.parentId`, which breaks the expected behavior when accessing request IDs from plugin contexts.

### Reproduction

```js
// In a plugin context
const response = {
  parentId: 'req_123',
  requestId: 'req_456'
}

// getRequestId() now returns 'req_456' instead of 'req_123'
const requestId = response.getRequestId()
console.log(requestId) // Expected: 'req_123', Got: 'req_456'
```

### Expected behavior

`getRequestId()` should return the `parentId` field (or an empty string if not available), not the `requestId` field. This is breaking existing plugins that rely on this method to get the correct request identifier.

### Additional context

This seems like it might have been changed recently. The method was previously returning `response.parentId || ''` which was the correct behavior for our use case.

---
Repository: /testbed
