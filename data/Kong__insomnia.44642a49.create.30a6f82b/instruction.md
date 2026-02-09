# Bug Report

### Describe the bug

I'm having an issue creating new GrpcRequest objects. When I try to create a request with a valid `parentId`, the request is created but all the properties I pass in are being ignored. The created request ends up empty except for default values.

### Reproduction

```js
const newRequest = create({
  parentId: 'wrk_123',
  name: 'My gRPC Request',
  url: 'grpc://localhost:50051',
  method: 'SayHello'
});

// Expected: newRequest should have name, url, method properties
// Actual: newRequest only has default values, all passed properties are missing
```

### Expected behavior

When calling `create()` with a patch object containing `parentId` and other properties, the created GrpcRequest should include all the properties from the patch object. Currently it seems like the patch data is being discarded.

### Additional context

This seems to have broken recently. Previously I could pass configuration when creating a new request and it would be applied correctly. Now I have to manually update the request after creation which is not ideal.

---
Repository: /testbed
