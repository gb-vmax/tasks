# Bug Report

### Describe the bug

I'm unable to create new gRPC requests in my workspace. Whenever I try to create a new gRPC request, I get an error saying "New GrpcRequest missing `parentId`" even though I'm providing a valid `parentId`.

### Reproduction

```js
// This throws an error even with parentId provided
const newRequest = create({
  parentId: 'wrk_123456',
  name: 'My gRPC Request'
});

// Error: New GrpcRequest missing `parentId`
```

### Expected behavior

Creating a gRPC request with a `parentId` should work without throwing an error. The validation should only fail when `parentId` is actually missing or undefined.

### Additional context

This seems to have broken recently - I was able to create gRPC requests before without any issues. Now every attempt to create a new gRPC request fails with this validation error.

---
Repository: /testbed
