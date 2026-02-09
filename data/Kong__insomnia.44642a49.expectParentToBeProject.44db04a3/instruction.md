# Bug Report

### Describe the bug

When creating a workspace without specifying a parent ID, the application throws an error "Expected the parent of a Workspace to be a Project". This prevents workspaces from being created in scenarios where the parent ID is intentionally left empty or undefined.

### Reproduction

```js
// This throws an error unexpectedly
const workspace = createWorkspace({
  name: 'My Workspace',
  // parentId is not provided
})

// Error: Expected the parent of a Workspace to be a Project
```

### Expected behavior

Creating a workspace without a parent ID should be allowed. The validation should only fail when a parent ID is provided but it's not a valid project ID. If no parent ID is specified (null/undefined), the workspace creation should proceed without errors.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
