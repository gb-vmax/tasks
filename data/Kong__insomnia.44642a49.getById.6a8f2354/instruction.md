# Bug Report

### Describe the bug

I'm experiencing an issue where gRPC requests are not being retrieved correctly by their ID. When trying to fetch a specific gRPC request using its exact ID, I'm getting unexpected results - sometimes it returns the wrong request or multiple requests instead of the single one I'm looking for.

### Reproduction

```js
// Create a gRPC request with ID 'req_abc123'
const request1 = await grpcRequest.create({
  _id: 'req_abc123',
  // ... other properties
});

// Create another request with similar ID 'req_abc123456'
const request2 = await grpcRequest.create({
  _id: 'req_abc123456',
  // ... other properties
});

// Try to get the first request by exact ID
const result = grpcRequest.getById('req_abc123');

// Expected: returns request1 only
// Actual: returns request1 OR both requests (inconsistent behavior)
```

### Expected behavior

`getById()` should return only the gRPC request with the exact matching `_id`. If I search for `req_abc123`, it should not return `req_abc123456` or any other request with a similar prefix.

### Additional context

This seems to have started recently. The function is supposed to do an exact match on the ID but appears to be doing some kind of pattern matching instead. This is particularly problematic when you have multiple requests with IDs that share common prefixes.

---
Repository: /testbed
