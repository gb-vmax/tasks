# Bug Report

### Describe the bug

I'm encountering an error when trying to create or work with workspaces that have a valid project as their parent. The application throws an error saying "Expected the parent of a Workspace to be a Project" even when the parentId is actually a valid project ID.

### Reproduction

```js
// When creating a workspace with a valid project parent
const workspace = {
  parentId: 'proj_abc123', // This is a valid project ID
  // ... other workspace properties
}

// Error is thrown: "Expected the parent of a Workspace to be a Project"
```

The validation logic seems to be rejecting valid project IDs instead of accepting them. This makes it impossible to create workspaces under projects, which breaks the normal workflow.

### Expected behavior

Workspaces should be able to have projects as their parent without throwing validation errors. The validation should only throw an error when the parentId is NOT a project ID.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
