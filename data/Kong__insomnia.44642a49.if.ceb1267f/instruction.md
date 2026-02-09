# Bug Report

### Describe the bug

When exporting data from a workspace, the plugin context is returning the wrong workspace. Instead of getting all workspaces under the active project, it's only returning a single workspace by ID.

### Reproduction

```js
// When trying to export data with an active project
const activeProjectId = 'proj_123';
const workspaces = await context.data.export.insomnia({
  includePrivate: false,
  format: 'json'
});

// Expected: All workspaces under the project
// Actual: Only the project itself (or single workspace)
```

### Steps to reproduce
1. Create a project with multiple workspaces
2. Set the project as active
3. Try to export data using the plugin API
4. Only one workspace is returned instead of all workspaces in the project

### Expected behavior

When an active project is set, the export should include all workspaces that belong to that project (using `findByParentId`), not just return the project/workspace by its ID.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might be a regression as the logic for finding workspaces by parent ID appears to have been changed to find by ID instead.

---
Repository: /testbed
