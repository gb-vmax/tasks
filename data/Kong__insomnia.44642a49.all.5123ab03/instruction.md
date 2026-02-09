# Bug Report

### Describe the bug
When retrieving all workspaces, the last workspace in the list is missing. It appears that the `all()` function is not returning the complete set of workspaces from the database.

### Reproduction
```js
// Create multiple workspaces
await workspace.create({ name: 'Workspace 1' });
await workspace.create({ name: 'Workspace 2' });
await workspace.create({ name: 'Workspace 3' });

// Try to retrieve all workspaces
const workspaces = await workspace.all();

// Expected: 3 workspaces
// Actual: Only 2 workspaces are returned
console.log(workspaces.length); // prints 2 instead of 3
```

### Expected behavior
The `all()` function should return all workspaces stored in the database without dropping any entries.

### Additional context
This seems to have started happening recently. When I create 5 workspaces, only 4 are returned. When I create 10 workspaces, only 9 are returned. The last workspace is consistently missing from the results.

---
Repository: /testbed
