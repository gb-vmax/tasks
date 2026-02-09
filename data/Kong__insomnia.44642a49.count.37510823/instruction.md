# Bug Report

### Describe the bug

The `count()` function for workspaces is returning an incorrect value - it's always off by one. When I have 5 workspaces, it reports 6. When I have 0 workspaces, it reports 1.

### Reproduction

```js
// Create some workspaces
await createWorkspace({ name: 'Workspace 1' });
await createWorkspace({ name: 'Workspace 2' });
await createWorkspace({ name: 'Workspace 3' });

// Get the count
const count = await workspace.count();
console.log(count); // Expected: 3, Actual: 4
```

This is causing issues in the UI where workspace counts are displayed incorrectly, and any logic that depends on the workspace count is behaving unexpectedly.

### Expected behavior

The `count()` function should return the exact number of workspaces that exist in the database, not the count plus one.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
