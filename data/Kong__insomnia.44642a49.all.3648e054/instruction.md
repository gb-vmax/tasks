# Bug Report

### Describe the bug

The `workspace.all()` function is only returning the first workspace instead of all workspaces. This breaks any functionality that expects to iterate over multiple workspaces.

### Reproduction

```js
import * as workspaceModel from './models/workspace';

// Create multiple workspaces
await workspaceModel.create({ name: 'Workspace 1' });
await workspaceModel.create({ name: 'Workspace 2' });
await workspaceModel.create({ name: 'Workspace 3' });

// Try to get all workspaces
const workspaces = await workspaceModel.all();

console.log(workspaces); // Expected: array with 3 workspaces
                         // Actual: single workspace object (first one only)
```

### Expected behavior

The `all()` function should return an array containing all workspaces from the database, not just the first one.

### Additional context

This seems to have broken recently. Any code that relies on getting multiple workspaces (like workspace switching, listing all projects, etc.) will now fail or show incomplete data.

---
Repository: /testbed
