# Bug Report

### Describe the bug

When duplicating gRPC requests, the operation fails with a syntax error. It looks like there's a problem with the code structure in the request duplication logic - the function seems to be defined incorrectly or there's some duplicate code that shouldn't be there.

### Reproduction

```js
// Try to duplicate a gRPC request
const originalRequest = {
  type: 'grpc',
  url: 'grpc://localhost:50051',
  protoFileId: 'proto_123',
  // ... other gRPC request fields
};

const duplicatedRequest = await duplicate(originalRequest, {
  name: 'Duplicated Request'
});
```

### Expected behavior

The gRPC request should be successfully duplicated with the provided patch applied. The duplicate should have a new ID and updated timestamps while preserving the original request's configuration.

### Actual behavior

The duplication fails and the application doesn't work properly. Looking at the code, it seems like there might be a syntax issue in the `duplicate` function where code is repeated or the function definition is malformed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
