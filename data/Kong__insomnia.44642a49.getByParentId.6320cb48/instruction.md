# Bug Report

### Describe the bug

The `getByParentId` function in the api-spec model is returning all API specs instead of filtering by the provided workspace ID. This causes the wrong API specs to be loaded when switching between workspaces.

### Reproduction

```js
// Create API specs for different workspaces
const workspace1 = 'workspace-1';
const workspace2 = 'workspace-2';

// Get API specs for workspace1
const specs = getByParentId(workspace1);

// Expected: Only specs for workspace1
// Actual: All API specs from all workspaces are returned
```

### Steps to reproduce
1. Create multiple workspaces with different API specs
2. Call `getByParentId()` with a specific workspace ID
3. The function returns all API specs instead of just the ones for that workspace

### Expected behavior
The function should only return API specs that belong to the specified workspace (parentId).

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when working with multiple workspaces as the wrong API specs are being displayed.

---
Repository: /testbed
