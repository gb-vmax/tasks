# Bug Report

### Describe the bug

After a recent update, I'm seeing stale data being returned when querying workspace metadata. When I update a workspace's metadata and then immediately fetch it again, the old values are still being returned instead of the updated ones.

### Reproduction

```js
// Get initial workspace meta
const meta = await getByParentId(workspaceId);
console.log(meta.someProperty); // prints "old value"

// Update the workspace meta
await updateByParentId(workspaceId, { someProperty: "new value" });

// Fetch again - expecting updated value
const updatedMeta = await getByParentId(workspaceId);
console.log(updatedMeta.someProperty); // still prints "old value" instead of "new value"
```

The issue seems to happen consistently when doing updates followed by reads. If I wait a few minutes between the update and the read, it works correctly.

### Expected behavior

After updating workspace metadata, subsequent calls to `getByParentId()` should return the most recent data immediately, not cached/stale values.

### Additional context

This appears to have started happening recently. I'm working on a feature that requires reading workspace metadata right after updating it, and the stale data is causing issues with the UI showing incorrect information.

---
Repository: /testbed
