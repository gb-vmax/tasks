# Bug Report

### Describe the bug

When creating multiple new gRPC requests, the metadata array is being shared across all instances. Modifying the metadata in one request affects all other requests that were created.

### Reproduction

```js
// Create first gRPC request
const request1 = init();
console.log(request1.metadata); // Shows default metadata

// Create second gRPC request
const request2 = init();

// Modify metadata in request2
request2.metadata[0].value = 'custom-value';

// Check request1 metadata - it's also changed!
console.log(request1.metadata[0].value); // Expected: 'application/grpc', Actual: 'custom-value'
```

### Expected behavior

Each gRPC request should have its own independent metadata array. Changes to one request's metadata should not affect other requests.

### Additional context

This appears to be happening because the default metadata array is being reused instead of creating a new array for each request instance. All requests end up referencing the same metadata objects in memory.

---
Repository: /testbed
