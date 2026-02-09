# Bug Report

### Describe the bug

When calling `getByParentId()` with a valid workspace parent ID, the function returns `null` instead of the expected workspace metadata. This appears to be a regression as it was working correctly before.

### Reproduction

```js
// Create a workspace with metadata
const workspace = await createWorkspace({ name: 'Test Workspace' });
const workspaceMeta = await createWorkspaceMeta({ parentId: workspace._id });

// Try to retrieve the metadata by parent ID
const result = await getByParentId(workspace._id);

// result is null, but should return the workspace metadata
console.log(result); // null
```

### Expected behavior

`getByParentId()` should return the workspace metadata object when called with a valid parent ID. The function should properly query the database using the parent ID and return the matching record.

### Additional context

This seems to have started happening recently. The workspace metadata is being created successfully, but retrieving it by parent ID no longer works. Other query methods seem unaffected.

---
Repository: /testbed
