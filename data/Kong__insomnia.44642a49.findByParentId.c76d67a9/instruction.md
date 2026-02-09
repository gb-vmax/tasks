# Bug Report

### Describe the bug

I'm experiencing an issue where workspaces aren't being retrieved correctly when searching by parent ID. The `findByParentId` function seems to be returning empty results even when workspaces with the specified parent ID definitely exist in the database.

### Reproduction

```js
// Create a workspace with a parent
const parentId = 'wrk_parent123';
const workspace = await workspace.create({ 
  parentId: parentId,
  name: 'Test Workspace'
});

// Try to find workspaces by parent ID
const workspaces = await workspace.findByParentId(parentId);

// Expected: Array with the workspace we just created
// Actual: Empty array []
console.log(workspaces); // []
```

### Expected behavior

The function should return all workspaces that have the matching `parentId`. In the example above, it should return an array containing the workspace we just created.

### Additional context

This seems to have started happening recently. I can confirm the workspaces are being saved correctly because I can retrieve them using `getById`, but `findByParentId` always returns empty results regardless of what parent ID I pass in.

---
Repository: /testbed
