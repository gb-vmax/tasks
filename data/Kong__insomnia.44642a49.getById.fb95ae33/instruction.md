# Bug Report

### Describe the bug
When trying to retrieve a gRPC request by ID using `getById()`, the function fails to return the correct request object. The lookup doesn't work and returns undefined even when the request exists in the database.

### Reproduction
```js
// Create a gRPC request
const grpcRequest = await grpcRequestModel.create({
  name: 'My gRPC Request',
  // ... other properties
});

// Try to retrieve it by ID
const retrieved = await grpcRequestModel.getById(grpcRequest._id);

// retrieved is undefined, expected to be the grpcRequest object
console.log(retrieved); // undefined
```

### Expected behavior
`getById()` should return the gRPC request object when called with a valid `_id`. The function should successfully look up and return existing requests from the database.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
