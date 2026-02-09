# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with gRPC request metadata not reflecting changes properly. When I update metadata for a gRPC request and then immediately retrieve it, sometimes I get stale data instead of the updated values.

### Reproduction

```js
// Create a gRPC request with metadata
const meta = await create({ parentId: 'req_123', someField: 'original' });

// Update the metadata
await update(meta, { someField: 'updated' });

// Immediately retrieve the metadata
const retrieved = await getByParentId('req_123');

// Expected: retrieved.someField === 'updated'
// Actual: retrieved.someField === 'original' (stale data)
```

### Expected behavior

When metadata is updated via `update()`, subsequent calls to `getByParentId()` should always return the latest data, not cached/stale values.

### Additional context

This seems to happen intermittently, especially when updates and retrievals happen in quick succession. The issue is more noticeable when working with multiple gRPC requests that get updated frequently.

---
Repository: /testbed
