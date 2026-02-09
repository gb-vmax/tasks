# Bug Report

### Describe the bug

I'm experiencing an issue with workspace metadata retrieval. When trying to get workspace metadata by parent ID, the function appears to be querying with the wrong field, which causes it to return incorrect or no results.

### Reproduction

```js
// Create a workspace with metadata
const workspace = await createWorkspace({ name: 'Test Workspace' });
const workspaceMeta = await createWorkspaceMeta({ parentId: workspace._id });

// Try to retrieve the metadata by parent ID
const meta = await getByParentId(workspace._id);

// meta is undefined or returns wrong data
console.log(meta); // Expected: workspaceMeta object, Actual: undefined or wrong object
```

### Expected behavior

`getByParentId()` should query the database using the `parentId` field to find workspace metadata that belongs to the specified workspace, and return the correct metadata object.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
