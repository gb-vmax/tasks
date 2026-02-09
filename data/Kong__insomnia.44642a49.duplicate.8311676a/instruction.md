# Bug Report

### Describe the bug
When trying to duplicate a WebSocket request, the application crashes or throws an error. The duplicate functionality that was previously working seems to be broken.

### Reproduction
```js
// Try to duplicate an existing WebSocket request
const originalRequest = {
  _id: 'ws_123',
  name: 'My WebSocket',
  metaSortKey: 100,
  // ... other properties
};

// Attempting to duplicate
await duplicate(originalRequest);
// Error occurs - function not implemented
```

### Expected behavior
The WebSocket request should be duplicated with:
- A new name appended with "(Copy)"
- A properly calculated metaSortKey positioned between the original and next request
- All other properties copied from the original request

### Additional context
This appears to affect the ability to duplicate WebSocket requests in the UI. The duplicate function seems to be missing its implementation, even though the function signature still exists.

---
Repository: /testbed
