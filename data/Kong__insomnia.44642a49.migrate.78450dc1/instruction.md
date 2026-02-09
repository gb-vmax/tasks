# Bug Report

### Describe the bug

After a recent update, gRPC requests are losing their `_id` property during migration. This causes issues when trying to reference or update existing gRPC requests, as the ID is essential for identifying and tracking these objects throughout the application.

### Reproduction

```js
const grpcRequest = {
  _id: 'req_123456',
  name: 'My gRPC Request',
  url: 'grpc://localhost:50051',
  // ... other properties
};

const migrated = migrate(grpcRequest);

console.log(migrated._id); // undefined - ID is missing!
console.log(grpcRequest._id); // 'req_123456' - original still has it
```

### Expected behavior

The `migrate()` function should preserve the `_id` property since it's a critical identifier for the request object. Without it, the application can't properly track or update existing gRPC requests.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
