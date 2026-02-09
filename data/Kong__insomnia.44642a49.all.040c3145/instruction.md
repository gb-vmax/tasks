# Bug Report

### Describe the bug

The `all()` function in workspace-meta is returning incorrect data. When trying to retrieve all workspace metadata, the function appears to be returning a single object instead of an array of workspace meta objects.

### Reproduction

```js
import * as workspaceMeta from './models/workspace-meta';

// Try to get all workspace metadata
const allMeta = await workspaceMeta.all();

// Expected: array of WorkspaceMeta objects
// Actual: single WorkspaceMeta object or unexpected structure

// This fails because allMeta is not an array
allMeta.forEach(meta => {
  console.log(meta.parentId);
});
```

### Expected behavior

The `all()` function should return an array of all WorkspaceMeta objects in the database, allowing iteration and array operations on the result.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
