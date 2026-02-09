# Bug Report

### Describe the bug

After a recent update, workspace metadata changes aren't being reflected immediately in the UI. When I update workspace settings or metadata, the changes don't show up until I restart the application or manually refresh.

### Reproduction

1. Open a workspace and modify its settings (e.g., change the name or description)
2. Navigate to another workspace
3. Navigate back to the original workspace
4. The changes are not visible - it still shows the old metadata

Another scenario:
```js
// Update workspace metadata
await updateByParentId(workspaceId, { activeActivity: 'debug' });

// Immediately fetch it back
const meta = await getByParentId(workspaceId);

// meta still contains old activeActivity value instead of 'debug'
```

### Expected behavior

When workspace metadata is updated via `updateByParentId()`, subsequent calls to `getByParentId()` should immediately return the updated data. The UI should reflect changes without requiring a restart.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues in our workflow where we frequently switch between workspaces and update settings. The stale data makes it difficult to know if changes were actually saved.

---
Repository: /testbed
