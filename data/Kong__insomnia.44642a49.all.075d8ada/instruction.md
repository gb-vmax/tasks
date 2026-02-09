# Bug Report

### Describe the bug

The `all()` function in workspace-meta is now returning an empty array when the database query returns valid results. Previously it would return all workspace metadata entries, but now it's filtering them out incorrectly and returning an empty array instead.

### Reproduction

```js
// Create some workspace metadata entries
await createWorkspaceMeta({ parentId: 'workspace1' });
await createWorkspaceMeta({ parentId: 'workspace2' });

// Try to retrieve all workspace metadata
const allMeta = all();

// Expected: Array with 2 workspace meta objects
// Actual: Empty array []
console.log(allMeta); // []
```

### Expected behavior

The `all()` function should return all workspace metadata entries from the database, not an empty array. When workspace metadata exists in the database, calling `all()` should return those entries.

### System Info
- Insomnia version: latest
- OS: All platforms affected

This is blocking our ability to load workspace settings and preferences. Any workspace-related functionality that depends on retrieving all metadata is currently broken.

---
Repository: /testbed
