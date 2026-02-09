# Bug Report

### Describe the bug

When trying to get or create an API spec for a workspace, duplicate specs are being created instead of returning the existing one. The function `getOrCreateForParentId` is creating new specs even when one already exists for the parent workspace.

### Reproduction

```js
// First call - creates a spec for workspace
const spec1 = await getOrCreateForParentId(workspaceId);

// Second call - should return the same spec, but creates a duplicate instead
const spec2 = await getOrCreateForParentId(workspaceId);

// spec1._id !== spec2._id (unexpected - should be the same)
```

### Expected behavior

The function should return the existing API spec if one already exists for the given workspace ID. It should only create a new spec if none exists.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
