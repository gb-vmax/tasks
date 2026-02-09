# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with gRPC request metadata not reflecting the latest changes. When I update a gRPC request's metadata using the `update()` function, subsequent calls to `getByParentId()` sometimes return stale data instead of the updated values.

### Reproduction

```js
// Create or get gRPC request metadata
const requestMeta = await getOrCreateByParentId(parentId);

// Update some metadata
await update(requestMeta, { 
  selectedMethod: 'newMethod',
  lastActive: Date.now() 
});

// Try to retrieve the updated metadata
const retrieved = await getByParentId(parentId);

// Retrieved metadata still shows old values
console.log(retrieved.selectedMethod); // Shows old value instead of 'newMethod'
```

### Expected behavior

When metadata is updated via the `update()` function, subsequent calls to `getByParentId()` should return the most recent data from the database, not cached or stale values.

### Additional context

This seems to happen intermittently, especially when multiple updates happen in quick succession. The issue is particularly noticeable when switching between different gRPC methods in the same request - the UI sometimes shows the previously selected method instead of the current one.

---
Repository: /testbed
