# Bug Report

### Describe the bug

I'm having an issue where `findByParentId()` is not returning the correct workspaces. When I call this function with a specific parent ID, it seems to be returning workspaces that don't match the parent ID I'm looking for, or returning an empty result when there should be matching workspaces.

### Reproduction

```js
// Create a workspace with a specific parent ID
const parentId = 'parent-123';
const workspace = await create({ parentId: parentId });

// Try to find workspaces by parent ID
const workspaces = findByParentId(parentId);

// Expected: Should return the workspace we just created
// Actual: Returns empty array or workspaces with different parent IDs
```

### Expected behavior

When calling `findByParentId(parentId)`, it should return all workspaces that have the specified `parentId`. The function should filter workspaces based on the parent ID parameter passed to it.

### Additional context

This seems to have broken recently. The function used to work correctly but now it's not filtering by the parent ID at all. It's affecting the ability to organize and retrieve nested workspaces properly.

---
Repository: /testbed
