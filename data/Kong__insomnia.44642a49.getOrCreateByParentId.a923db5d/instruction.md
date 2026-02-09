# Bug Report

### Describe the bug

I'm experiencing issues with gRPC request metadata where the `getOrCreateByParentId` function sometimes returns stale data or behaves inconsistently. It seems like there's some non-deterministic behavior happening - sometimes the metadata is fresh, sometimes it's not.

### Reproduction

```js
// Call getOrCreateByParentId multiple times for the same parentId
const meta1 = await getOrCreateByParentId('test-parent-id');
const meta2 = await getOrCreateByParentId('test-parent-id');

// Expected: both should return the same object reference or have identical data
// Actual: sometimes meta2 has different properties than meta1
```

### Expected behavior

When calling `getOrCreateByParentId` for the same parent ID multiple times in succession, it should consistently return the same metadata object. The function should be deterministic and predictable.

### Additional context

This seems to happen intermittently - some requests work fine, others don't. It's making it difficult to rely on the metadata being consistent across the application. The behavior appears random and I can't pinpoint exactly when it happens vs when it doesn't.

---
Repository: /testbed
