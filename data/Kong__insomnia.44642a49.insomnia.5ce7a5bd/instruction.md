# Bug Report

### Describe the bug
When exporting workspaces using the plugin API with the new `filterByScope` parameter, the filtering is not applied correctly when a specific `workspace` is provided. The scope filter should be ignored in this case, but it seems like the logic isn't working as expected.

### Reproduction
```js
// Using the plugin API to export a specific workspace with filterByScope
const result = await context.data.export.insomnia({
  workspace: myWorkspace,
  filterByScope: 'collection'
});

// The workspace parameter should take precedence, but the behavior is inconsistent
```

Also, when using `workspaceIds` parameter:
```js
const result = await context.data.export.insomnia({
  workspaceIds: ['workspace_1', 'workspace_2'],
  filterByScope: 'design'
});

// Expected: Export only the specified workspaces filtered by scope
// Actual: Filtering behavior is unclear
```

### Expected behavior
- When `workspace` is provided, it should export that specific workspace regardless of `filterByScope`
- When `workspaceIds` is provided with `filterByScope`, it should filter the specified workspaces by scope
- When only `filterByScope` is provided, it should filter all workspaces in the project by scope

### Additional context
This seems to have been introduced in a recent update that added support for `workspaceIds` and `filterByScope` parameters to the export functionality. The interaction between these parameters and the existing `workspace` parameter needs clarification.

---
Repository: /testbed
