# Bug Report

### Describe the bug

I'm experiencing an issue where workspaces aren't being retrieved correctly when searching by parent ID. When I try to find workspaces that belong to a specific parent, the query returns no results even though I know workspaces with that parent ID exist in the database.

### Reproduction

```js
const parentId = 'some-parent-id';
const workspaces = findByParentId(parentId);

// Expected: Array of workspaces with matching parentId
// Actual: Empty array (no workspaces found)
```

Steps to reproduce:
1. Create a workspace with a specific parent ID
2. Try to retrieve it using `findByParentId()` with that parent ID
3. The function returns an empty array instead of the expected workspaces

### Expected behavior

The `findByParentId()` function should return all workspaces that have the specified parent ID. This was working correctly before, but now it seems like the query isn't matching any records.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
