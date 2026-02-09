# Bug Report

### Describe the bug

After a recent update, the request update function appears to be broken. When trying to update a request object, I'm getting syntax errors and the update operation fails completely.

### Reproduction

```js
const request = {
  _id: 'req_123',
  name: 'My Request',
  url: 'https://example.com',
  method: 'GET',
  created: 1234567890,
  modified: 1234567890
};

// Try to update the request
await update(request, { name: 'Updated Request' });
// This throws an error now
```

### Expected behavior

The request should be updated successfully with the new name, and the modified timestamp should be automatically updated. The operation worked fine before the recent changes.

### Additional context

This seems to affect all request types (regular requests, gRPC requests, and WebSocket requests). The code appears to have some syntax issues that prevent it from running at all.

---
Repository: /testbed
