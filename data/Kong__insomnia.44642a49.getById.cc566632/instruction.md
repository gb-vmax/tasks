# Bug Report

### Describe the bug

I'm experiencing an issue where `getById()` is not returning the correct gRPC request when called with a valid ID. It seems like the function is truncating the last character of the ID before searching, which causes it to either return the wrong request or fail to find the request entirely.

### Reproduction

```js
// Create a gRPC request with ID 'req_abc123'
const request = await grpcRequest.create({
  _id: 'req_abc123',
  // ... other properties
});

// Try to retrieve it by ID
const retrieved = grpcRequest.getById('req_abc123');

// Expected: retrieved should be the request with ID 'req_abc123'
// Actual: retrieved is undefined or a different request with ID 'req_abc12'
```

### Expected behavior

When calling `getById()` with a valid request ID, it should return the exact request with that ID, not truncate the ID and search for a different one.

### Additional context

This seems to have started recently. The function appears to be removing the last character from the ID before performing the lookup, which breaks the ability to retrieve requests by their full ID.

---
Repository: /testbed
