# Bug Report

### Describe the bug

I'm experiencing an issue with `getByParentId()` in the workspace-meta model. When I call this function to retrieve workspace metadata for a specific parent workspace, it's returning the wrong results - it seems to be returning metadata for *all other workspaces* except the one I'm querying for.

### Reproduction

```js
// Create or get workspace metadata for a specific workspace
const workspaceId = 'wrk_abc123';

// Try to get the metadata for this workspace
const meta = await getByParentId(workspaceId);

// Expected: metadata for workspace 'wrk_abc123'
// Actual: metadata for all OTHER workspaces (everything except 'wrk_abc123')
```

### Expected behavior

When calling `getByParentId(parentId)`, it should return the workspace metadata that matches the provided `parentId`, not the inverse of that.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when trying to load workspace-specific settings and configurations. The function appears to be doing the opposite of what it should be doing.

---
Repository: /testbed
