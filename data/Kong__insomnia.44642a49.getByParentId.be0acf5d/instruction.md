# Bug Report

### Describe the bug

I'm experiencing an issue with `getByParentId()` function where it's not filtering results correctly. The function seems to be returning metadata records that don't match the expected type, even when called with a valid gRPC request parent ID.

### Reproduction

```js
// Call getByParentId with a valid gRPC request ID
const parentId = 'req_abc123';
const meta = getByParentId(parentId);

// The function returns records that aren't necessarily GrpcRequestMeta type
// It appears to be ignoring the type parameter
```

### Expected behavior

The function should only return `GrpcRequestMeta` records that match both:
1. The specified `parentId`
2. The correct document type

Currently it seems like the type filtering is being skipped, which could lead to returning incorrect metadata objects or objects from other collections.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
