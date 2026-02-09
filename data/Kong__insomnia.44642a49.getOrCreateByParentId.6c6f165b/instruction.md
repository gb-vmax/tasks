# Bug Report

### Describe the bug

When working with gRPC requests, I'm getting duplicate entries created in the database. It seems like `getOrCreateByParentId` is creating a new meta object even when one already exists for the parent ID.

### Reproduction

```js
// First call - creates a new grpc-request-meta
const meta1 = await getOrCreateByParentId('request-123');

// Second call with same parent ID - should return existing meta
const meta2 = await getOrCreateByParentId('request-123');

// Expected: meta1._id === meta2._id
// Actual: meta1._id !== meta2._id (two different objects created)
```

### Expected behavior

The function should check if a meta object already exists for the given `parentId` before creating a new one. On subsequent calls with the same `parentId`, it should return the existing meta object instead of creating duplicates.

### Additional context

This is causing issues where multiple gRPC request meta entries are being created for the same request, which leads to inconsistent state and potential data conflicts. The function name suggests it should "get or create" but it appears to always be creating new entries.

---
Repository: /testbed
