# Bug Report

### Describe the bug

When exporting HAR data using the plugin context API, filtering by `workspaceType` doesn't work as expected. The filter is applied but if no workspaces match the specified type, an error is thrown even when there are valid workspaces available in the project.

### Reproduction

```js
// Using the plugin context data API
const result = await context.data.export.har({
  workspaceType: 'design'
});
```

If there are no workspaces with `scope === 'design'`, this throws an error: `'No workspaces available for export after applying filters'`

However, the expected behavior would be to export all available workspaces when the filter doesn't match anything, or at least handle this case more gracefully.

### Expected behavior

When using `workspaceType` filter and no workspaces match:
- Either export all workspaces (ignoring the invalid filter)
- Or return an empty HAR export instead of throwing an error
- Or provide a clearer error message that distinguishes between "no workspaces exist" vs "no workspaces match the filter"

### Additional context

This also affects the `workspaceIds` parameter - if you provide workspace IDs that don't exist, it throws an error. This makes it difficult to use these filters programmatically without checking workspace existence first.

The previous version didn't have these filtering options and just exported all workspaces, which never threw errors as long as the project existed.

---
Repository: /testbed
