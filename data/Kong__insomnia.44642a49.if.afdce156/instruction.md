# Bug Report

### Describe the bug

After a recent update, the data export functionality seems to be broken. When trying to export workspace data, the operation appears to hang indefinitely and never completes. This is blocking our ability to backup and migrate workspace configurations.

### Reproduction

```js
// Attempting to export workspace data
const workspaces = await data.export.insomnia({
  includePrivate: false,
  format: 'json',
  workspace: workspaceId
});

// The promise never resolves
console.log(workspaces); // Never reached
```

### Steps to reproduce:
1. Open a project with multiple workspaces
2. Attempt to export workspace data using the plugin API
3. The export operation hangs and doesn't complete

### Expected behavior

The export should complete successfully and return the workspace data. Previously this worked fine and would return the data immediately.

### Additional context

This seems to have started happening after some changes to the data context module. The issue occurs consistently across different projects and workspaces.

---
Repository: /testbed
