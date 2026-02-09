# Bug Report

### Describe the bug
The `updateByParentId` function in workspace-meta is not correctly updating workspace metadata. When calling this function to update workspace settings, the changes don't seem to persist or apply properly.

### Reproduction
```js
// Try to update workspace metadata by parent ID
await updateByParentId('workspace-123', {
  activeActivity: 'debug',
  sidebarWidth: 300
});

// Fetch the metadata again
const meta = await getByParentId('workspace-123');

// The metadata doesn't reflect the updates
console.log(meta.activeActivity); // Expected: 'debug', but changes not applied
```

### Expected behavior
When calling `updateByParentId` with a patch object, the workspace metadata should be updated with the new values and the updated metadata should be returned.

### Additional context
This affects workspace settings persistence - things like sidebar width, active activity, and other workspace-specific preferences aren't being saved correctly when using this function.

---
Repository: /testbed
