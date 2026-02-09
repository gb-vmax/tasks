# Bug Report

### Describe the bug

When creating a new workspace, the workspace type is not being set correctly. Instead of getting a proper workspace object with the correct `type` field, the created workspace seems to be missing or has an incorrect type value.

### Reproduction

```js
// Try to create a workspace with a parent project
const workspace = await create({
  parentId: 'proj_123',
  name: 'My Workspace'
});

// The workspace is created but the type field is not set properly
console.log(workspace.type); // undefined or incorrect value
```

### Expected behavior

The created workspace should have the correct `type` field set (e.g., `'Workspace'`). The workspace object should be properly initialized with all required fields including the type.

### Additional context

This seems to affect workspace creation across the application. Any code that relies on checking the workspace type might fail or behave unexpectedly.

---
Repository: /testbed
