# Bug Report

### Describe the bug

I'm experiencing an issue where gRPC requests cannot be retrieved by their ID. When trying to fetch a specific gRPC request using its ID, the function returns `null` or `undefined` instead of the expected request object.

### Reproduction

```js
// Create or get a gRPC request with a known ID
const requestId = 'req_abc123';

// Try to retrieve the request by ID
const request = getById(requestId);

// request is null/undefined even though the ID exists in the database
console.log(request); // Expected: GrpcRequest object, Actual: null
```

### Expected behavior

The `getById()` function should return the gRPC request object when a valid ID is passed. The request exists in the database but cannot be retrieved.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently as I was able to fetch gRPC requests by ID before. Any help would be appreciated!

---
Repository: /testbed
