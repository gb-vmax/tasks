# Bug Report

### Describe the bug

When calling `getWorkspaces()` without an `activeProjectId`, the function is returning workspaces that have a `parentId` instead of workspaces without one. This seems backwards - when no active project is specified, I'd expect to get workspaces that aren't tied to any project (i.e., those with no `parentId`).

### Reproduction

```js
// Call getWorkspaces without a project ID
const workspaces = await getWorkspaces();

// Expected: workspaces without a parentId
// Actual: workspaces WITH a parentId (filtered to only include those)
```

### Expected behavior

When `activeProjectId` is not provided, the function should return workspaces that don't belong to any project (workspaces where `parentId` is null/undefined), not filter to only include workspaces that DO have a parent.

The current behavior filters to `workspaces.filter(w => w.parentId)` which keeps only workspaces with a parent, but logically it should be filtering to workspaces WITHOUT a parent when no project is specified.

### Additional context

This is affecting workspace discovery when no specific project context is available. The defensive code path comment mentions this is for cases without an active project, so returning only workspaces that belong TO a project doesn't make sense in that scenario.

---
Repository: /testbed
