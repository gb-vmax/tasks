# Bug Report

### Describe the bug

After a recent update, workspace metadata changes are not being reflected immediately in the UI. When I update workspace settings or metadata, the changes don't appear until I restart the application or manually refresh. It seems like the application is showing stale/cached data instead of the updated values.

### Reproduction

1. Open a workspace and modify its metadata (e.g., change active environment, update sidebar visibility settings)
2. Use `updateByParentId()` to save the changes
3. Immediately call `getByParentId()` with the same workspace ID
4. The returned data still shows the old values instead of the updated ones

This is causing issues where users think their changes didn't save, or they see outdated information when switching between workspaces.

### Expected behavior

When workspace metadata is updated via `updateByParentId()`, subsequent calls to `getByParentId()` should immediately return the updated data, not cached stale values.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
