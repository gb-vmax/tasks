# Bug Report

### Describe the bug

The `create()` function for GrpcRequest is not working properly. When trying to create a new gRPC request with a valid `parentId`, it's throwing an error saying the parentId is missing even though it was provided.

### Reproduction

```js
const newRequest = {
  parentId: 'wrk_123',
  name: 'My gRPC Request',
  url: 'grpc://localhost:50051'
}

// This throws: "New GrpcRequest missing `parentId`"
const result = create(newRequest)
```

### Expected behavior

The function should successfully create a new GrpcRequest when a valid `parentId` is provided in the patch object. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context

This seems to have broken recently. The validation logic appears to be checking the wrong condition, causing it to fail even with valid input.

---
Repository: /testbed
