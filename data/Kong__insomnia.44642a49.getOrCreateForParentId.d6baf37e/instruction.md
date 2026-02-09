# Bug Report

### Describe the bug
When calling `getOrCreateForParentId()` for an API spec, it's creating duplicate specs instead of returning the existing one. Every time the function is called, a new spec is created even when one already exists for the workspace.

### Reproduction
```js
const workspaceId = 'wrk_123';

// First call - creates a spec
const spec1 = await getOrCreateForParentId(workspaceId);

// Second call - should return the same spec, but creates a new one instead
const spec2 = await getOrCreateForParentId(workspaceId);

// spec1._id !== spec2._id (they should be the same!)
```

### Expected behavior
The function should return the existing API spec if one already exists for the workspace, and only create a new one if it doesn't exist. Multiple calls with the same `workspaceId` should return the same spec object.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
