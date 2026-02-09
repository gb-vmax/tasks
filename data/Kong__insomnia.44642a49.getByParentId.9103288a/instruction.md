# Bug Report

### Describe the bug
When trying to retrieve gRPC request metadata by parent ID, the function returns `null` or undefined instead of the expected metadata object. This breaks the ability to load saved gRPC request configurations.

### Reproduction
```js
// Create a gRPC request with metadata
const grpcRequest = { _id: 'req_123', type: 'GrpcRequest' };
const metadata = {
  parentId: 'req_123',
  // ... other metadata fields
};

// Try to retrieve metadata by parent ID
const result = getByParentId('req_123');
// result is null/undefined instead of returning the metadata object
```

### Expected behavior
The `getByParentId()` function should return the gRPC request metadata associated with the given parent ID. Previously saved metadata should be retrievable when loading gRPC requests.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
