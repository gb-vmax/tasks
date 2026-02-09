# Bug Report

### Describe the bug

After a recent update, duplicating requests is completely broken. When trying to duplicate any type of request (regular HTTP, gRPC, or WebSocket), the application throws an error or the duplication fails silently.

### Reproduction

```js
// Attempting to duplicate a request
const originalRequest = {
  _id: 'req_123',
  name: 'My Request',
  url: 'https://api.example.com',
  method: 'GET'
};

// This now fails
const duplicatedRequest = await duplicate(originalRequest, {
  name: 'My Request (Copy)'
});
```

### Expected behavior

The request should be duplicated successfully with the patched properties applied. This was working fine before and is now completely broken for all request types.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
