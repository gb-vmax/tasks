# Bug Report

### Describe the bug

The `findByParentId()` function is not returning the correct workspaces. Instead of finding all workspaces that have a specific `parentId`, it seems to be searching by `id` field which returns completely wrong results.

### Reproduction

```js
// Create a parent workspace
const parent = await workspace.create({ name: 'Parent' });

// Create child workspaces
const child1 = await workspace.create({ name: 'Child 1', parentId: parent._id });
const child2 = await workspace.create({ name: 'Child 2', parentId: parent._id });

// Try to find all workspaces with this parent
const children = await workspace.findByParentId(parent._id);

// Expected: Should return [child1, child2]
// Actual: Returns incorrect results or empty array
```

### Expected behavior

`findByParentId()` should return all workspace objects that have the specified `parentId`. This is necessary for properly organizing and displaying workspace hierarchies in the UI.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
