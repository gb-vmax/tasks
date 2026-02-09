# Bug Report

### Describe the bug

The `data.export.har()` function doesn't properly handle the `workspaceIds` parameter when exporting HAR files. When passing specific workspace IDs, the function falls back to exporting all workspaces in the project instead of just the requested ones.

### Reproduction

```js
// Try to export HAR for specific workspaces
await context.data.export.har({
  workspaceIds: ['workspace_123', 'workspace_456']
})

// Expected: Only exports HAR for the two specified workspaces
// Actual: Exports HAR for all workspaces in the active project
```

### Expected behavior

When `workspaceIds` is provided with valid workspace IDs, the HAR export should only include those specific workspaces. If the IDs don't match any workspaces, it should probably either return an empty export or throw an error, but not silently fall back to exporting everything.

### Additional context

This seems to be a regression - the function previously only supported the `workspace` parameter (single workspace) but the new `workspaceIds` parameter isn't working as expected. The fallback behavior makes it difficult to know if the export actually succeeded for the intended workspaces or if it just exported everything.

---
Repository: /testbed
