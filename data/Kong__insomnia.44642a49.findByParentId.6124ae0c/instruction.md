# Bug Report

### Describe the bug
When trying to find workspaces by parent ID, the function returns incorrect results. It appears to be returning workspaces that DON'T match the parent ID instead of the ones that do. Additionally, even when results are found, only the first result is returned instead of all matching workspaces.

### Reproduction
```js
// Create some workspaces with the same parent ID
const parentId = 'parent-123';
await create({ parentId: parentId, name: 'Workspace 1' });
await create({ parentId: parentId, name: 'Workspace 2' });
await create({ parentId: 'other-parent', name: 'Workspace 3' });

// Try to find all workspaces with parentId 'parent-123'
const workspaces = findByParentId('parent-123');

// Expected: Should return Workspace 1 and Workspace 2
// Actual: Returns wrong workspaces or only one workspace
```

### Expected behavior
`findByParentId()` should return all workspaces that have the specified parent ID, not workspaces with different parent IDs. If there are multiple workspaces with the same parent, all of them should be returned.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
