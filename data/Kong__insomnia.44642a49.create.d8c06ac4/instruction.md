# Bug Report

### Describe the bug

I'm unable to create new gRPC requests in my workspace. Whenever I try to create a gRPC request with a valid parent ID, I get an error saying "New GrpcRequest missing `parentId`" even though I'm definitely providing one.

### Reproduction

```js
// This throws an error even though parentId is provided
const grpcRequest = create({
  parentId: 'wrk_123456',
  name: 'My gRPC Request'
});
// Error: New GrpcRequest missing `parentId`
```

### Expected behavior

The gRPC request should be created successfully when a valid `parentId` is provided. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context

This seems to have started happening recently. I can't create any new gRPC requests in my project anymore because of this validation error.

---
Repository: /testbed
