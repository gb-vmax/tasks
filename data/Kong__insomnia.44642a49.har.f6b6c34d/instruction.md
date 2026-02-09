# Bug Report

### Describe the bug

When exporting HAR files using the data context plugin, the new filtering and sorting options don't work as expected. Specifically, when trying to filter workspaces by name or type, or sort them, the HAR export still includes all workspaces in the original order.

### Reproduction

```js
// Try to export HAR with filtering by name
await context.data.export.har({
  filterByName: 'test',
  sortBy: 'name'
});

// Expected: Only workspaces matching 'test' should be exported, sorted by name
// Actual: All workspaces are exported in original order
```

Also noticed that when providing a specific workspace, the filtering and sorting options are ignored (which might be intentional but isn't documented).

### Steps to reproduce:
1. Create multiple workspaces with different names
2. Use the har export function with filterByName parameter
3. Check the exported HAR file - it contains all workspaces instead of filtered ones

### Expected behavior

The HAR export should respect the filtering and sorting parameters:
- `filterByName` should filter workspaces by name pattern (case-insensitive)
- `filterByType` should filter by workspace scope
- `sortBy` should sort workspaces by the specified field (name, created, or modified)

### Additional context

This seems to have been introduced in a recent update that added these new export options. The filtering and sorting logic appears to be in place but doesn't seem to be applied correctly to the workspace list before export.

---
Repository: /testbed
