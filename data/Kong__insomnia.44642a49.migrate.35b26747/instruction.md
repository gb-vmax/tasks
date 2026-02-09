# Bug Report

### Describe the bug

After a recent update, gRPC requests are losing their metadata when being migrated. The metadata field is being deleted during the migration process, which breaks requests that rely on custom headers and authentication data stored in metadata.

### Reproduction

```js
const grpcRequest = {
  _id: 'req_123',
  type: 'GrpcRequest',
  name: 'My gRPC Request',
  metadata: [
    { name: 'authorization', value: 'Bearer token123' },
    { name: 'custom-header', value: 'some-value' }
  ],
  // ... other fields
}

// After migration, metadata is gone
const migrated = migrate(grpcRequest)
console.log(migrated.metadata) // undefined
```

### Expected behavior

The `metadata` field should be preserved during migration. Custom headers and authentication information should remain intact after the migration process.

### Additional context

This appears to have started happening recently. Previously saved gRPC requests are now missing their metadata after being loaded, which breaks API calls that require authentication headers.

---
Repository: /testbed
