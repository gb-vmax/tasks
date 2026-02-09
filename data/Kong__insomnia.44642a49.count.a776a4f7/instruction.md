# Bug Report

### Describe the bug

The `count()` function for workspaces is returning an incorrect count - it's always one less than the actual number of workspaces in the database.

### Reproduction

```js
// Create 3 workspaces
await workspace.create({ name: 'Workspace 1' });
await workspace.create({ name: 'Workspace 2' });
await workspace.create({ name: 'Workspace 3' });

// Check the count
const total = await workspace.count();
console.log(total); // Outputs: 2 (expected: 3)
```

The count is consistently off by one. If I have 5 workspaces, it returns 4. If I have 1 workspace, it returns 0.

### Expected behavior

`workspace.count()` should return the actual number of workspaces in the database, not one less than the actual count.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
