# Bug Report

### Describe the bug

When creating a workspace without a parent (parentId is `null` or `undefined`), an error is thrown unexpectedly: "Expected the parent of a Workspace to be a Project". This prevents workspaces from being created in scenarios where they shouldn't require a parent project.

### Reproduction

```js
// This throws an error but shouldn't
const workspace = createWorkspace({
  parentId: null,
  // ... other properties
});

// Also throws an error
const workspace2 = createWorkspace({
  parentId: undefined,
  // ... other properties
});
```

### Expected behavior

Workspaces should be allowed to have `null` or `undefined` as their `parentId` without throwing an error. The validation should only fail when a `parentId` is provided but it's not a valid project ID.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
