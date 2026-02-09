# Bug Report

### Describe the bug

The `getByParentId` function in workspace-meta is not returning the correct workspace metadata. When I call this function with a valid workspace parent ID, it returns null or undefined instead of the expected workspace meta object.

### Reproduction

```js
const workspaceId = 'wrk_abc123';

// Try to get workspace meta by parent ID
const workspaceMeta = await getByParentId(workspaceId);

console.log(workspaceMeta); // Expected: workspace meta object, Actual: null/undefined
```

### Expected behavior

The function should return the workspace metadata object associated with the given parent ID. This worked correctly in previous versions but seems to have broken recently.

### Additional context

This is affecting workspace synchronization and causing issues when trying to access workspace-specific settings. The workspace itself exists and has metadata, but the lookup function isn't finding it.

---
Repository: /testbed
