# Bug Report

### Describe the bug

I'm encountering an error when trying to create or work with gRPC request metadata. The application throws an error saying "Expected the parent of GrpcRequestMeta to be a GrpcRequest" even when the parent is actually a valid GrpcRequest.

### Reproduction

```js
// When creating gRPC request metadata with a valid gRPC request parent
const grpcRequest = createGrpcRequest();
const grpcRequestMeta = createGrpcRequestMeta({
  parentId: grpcRequest._id  // This is a valid gRPC request ID
});

// Error is thrown: "Expected the parent of GrpcRequestMeta to be a GrpcRequest"
```

### Expected behavior

The gRPC request metadata should be created successfully when the parent is a valid GrpcRequest. The error should only be thrown when the parent is NOT a GrpcRequest.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
