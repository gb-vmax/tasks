# Bug Report

### Describe the bug

The `data.export.har()` plugin API is not respecting the `workspaceType` filter when a specific workspace is provided. When calling the function with both `workspace` and `workspaceType` parameters, the `workspaceType` filter is ignored and the export proceeds regardless of whether the workspace matches the specified type.

### Reproduction

```js
// Export HAR with both workspace and workspaceType specified
await context.data.export.har({
  workspace: myDesignWorkspace,
  workspaceType: 'collection'
});

// Expected: Should not export since workspace type doesn't match
// Actual: Exports the workspace anyway, ignoring the workspaceType filter
```

### Expected behavior

When both `workspace` and `workspaceType` are provided, the function should validate that the workspace matches the specified type before exporting. If the workspace type doesn't match, it should either skip the export or return an empty result.

Currently the filter logic only applies when `workspace` is not provided:
```js
if (workspaceType && !workspace) {
  // filtering logic
}
```

This means providing a specific workspace bypasses the type filter entirely.

### System Info
- Insomnia version: latest
- Plugin API: data.export.har

---
Repository: /testbed
