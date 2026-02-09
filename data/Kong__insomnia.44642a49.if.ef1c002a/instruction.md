# Bug Report

### Describe the bug

I'm experiencing an issue where gRPC requests are not being retrieved correctly. When I try to fetch a gRPC request by its ID, the application seems to skip the gRPC check entirely and either returns null or tries to treat it as a different request type.

### Reproduction

```js
// Create or get a gRPC request ID
const grpcRequestId = 'grpc_123456';

// Try to fetch the gRPC request
const request = await getById(grpcRequestId);

// request is null or wrong type, even though the gRPC request exists
console.log(request); // null or incorrect request type
```

### Expected behavior

When calling `getById()` with a valid gRPC request ID, it should return the corresponding gRPC request object. The function should properly check if the ID belongs to a gRPC request and retrieve it from the correct model.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started recently. The gRPC requests exist in the database but the retrieval logic isn't working as expected.

---
Repository: /testbed
