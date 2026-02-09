# Bug Report

### Describe the bug

I'm encountering an issue with gRPC request metadata handling. When working with gRPC requests, the metadata seems to be getting cleared or not persisted correctly. The application appears to be treating valid metadata objects as null/undefined in certain scenarios.

### Reproduction

```js
// Create a gRPC request with metadata
const grpcMeta = {
  requestId: 'abc123',
  selectedMethod: '/api.Service/Method',
  // ... other metadata fields
}

// After migration or update, the metadata is lost
// Expected: metadata should be preserved
// Actual: metadata becomes null/undefined
```

### Expected behavior

gRPC request metadata should be properly maintained and migrated. Valid metadata objects should not be cleared or converted to null/undefined values during processing.

### System Info

- Insomnia version: latest
- Platform: Desktop app

This seems to have started happening recently. The metadata was working fine before, but now it's not being handled correctly when the request is loaded or updated.

---
Repository: /testbed
