# Bug Report

### Describe the bug

I'm getting an error when trying to create a new GrpcRequestMeta without a `parentId`. The error message says "New GrpcRequestMeta missing `parentId`" but this is happening even when I'm providing a valid `parentId`.

### Reproduction

```js
// This throws an error even though parentId is provided
const meta = create({
  parentId: 'grpc_request_123'
});
// Error: New GrpcRequestMeta missing `parentId`
```

### Expected behavior

The GrpcRequestMeta should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
