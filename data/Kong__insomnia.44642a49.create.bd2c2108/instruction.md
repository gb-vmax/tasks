# Bug Report

### Describe the bug

When creating a workspace with a `parentId`, the parent ID is not being saved to the database. The workspace gets created successfully, but the `parentId` field is missing from the created document, which breaks the parent-child relationship between projects and workspaces.

### Reproduction

```js
const workspace = await create({
  name: 'My Workspace',
  parentId: 'proj_abc123'
});

console.log(workspace.parentId); // undefined (expected: 'proj_abc123')
```

### Steps to reproduce:
1. Create a workspace with a parentId specified
2. Check the created workspace object
3. The parentId field is missing even though it was provided

### Expected behavior

The workspace should be created with the `parentId` field preserved. The parent-child relationship should be maintained so that workspaces are properly associated with their parent projects.

### Additional context

This seems to have broken recently. Workspaces are now being created as orphaned objects without their parent reference, which causes issues when trying to query workspaces by parent ID or display them in the project hierarchy.

---
Repository: /testbed
