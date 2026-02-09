# Bug Report

### Describe the bug

When creating or updating a workspace with a valid parent project ID, the application throws an error "Expected the parent of a Workspace to be a Project" even though the parent is actually a valid project.

### Reproduction

```js
// Create a workspace with a valid project parent
const workspace = {
  parentId: 'proj_abc123', // valid project ID
  name: 'My Workspace'
}

// This throws an error unexpectedly
createWorkspace(workspace)
// Error: Expected the parent of a Workspace to be a Project
```

### Expected behavior

The workspace should be created successfully when provided with a valid project ID as the parent. The validation should only throw an error when the parent ID exists but is NOT a project ID.

### Additional context

This seems to affect any operation that validates workspace parent IDs. The error is thrown even when the parentId is correctly formatted as a project ID.

---
Repository: /testbed
