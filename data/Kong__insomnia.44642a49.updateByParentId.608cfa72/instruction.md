# Bug Report

### Describe the bug

When calling `updateByParentId()` to update workspace metadata, the function returns stale data instead of the updated values. The returned object still contains the old property values even though the update was applied to the database.

### Reproduction

```js
// Get initial workspace meta
const meta = await getByParentId(workspaceId);
console.log(meta.someProperty); // Output: "old value"

// Update the property
const updated = await updateByParentId(workspaceId, { someProperty: "new value" });
console.log(updated.someProperty); // Expected: "new value", Actual: "old value"

// Fetching again shows the update was applied
const refetched = await getByParentId(workspaceId);
console.log(refetched.someProperty); // Output: "new value"
```

### Expected behavior

The `updateByParentId()` function should return the updated workspace metadata object with all the new values applied, not the stale object from before the update.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
