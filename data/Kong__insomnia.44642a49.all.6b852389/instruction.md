# Bug Report

### Describe the bug

When fetching all workspaces using the `all()` function, the last workspace in the collection is missing from the returned results. This appears to be a recent regression as it was working correctly before.

### Reproduction

```js
// Create multiple workspaces
await workspace.create({ name: 'Workspace 1' });
await workspace.create({ name: 'Workspace 2' });
await workspace.create({ name: 'Workspace 3' });

// Fetch all workspaces
const allWorkspaces = await workspace.all();

// Expected: 3 workspaces
// Actual: 2 workspaces (last one is missing)
console.log(allWorkspaces.length); // prints 2 instead of 3
```

### Expected behavior

The `all()` function should return all workspaces from the database, including the last one. If there are 3 workspaces created, all 3 should be returned.

### Additional context

This is causing issues in the workspace list UI where the most recently created workspace doesn't appear until the app is restarted or the list is refreshed multiple times.

---
Repository: /testbed
