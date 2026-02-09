# Bug Report

### Describe the bug
When trying to retrieve a gRPC request by ID using `getById()`, the function fails to return the expected request object. It seems like the query is not matching correctly even when a valid ID is provided.

### Reproduction
```js
// Assume we have a valid gRPC request with ID "req_123abc"
const requestId = "req_123abc";

// Try to retrieve the request
const grpcRequest = getById(requestId);

// Returns null or undefined instead of the expected request object
console.log(grpcRequest); // Expected: GrpcRequest object, Actual: null/undefined
```

### Expected behavior
The `getById()` function should return the gRPC request object when provided with a valid request ID. The query should match against the `_id` field correctly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
