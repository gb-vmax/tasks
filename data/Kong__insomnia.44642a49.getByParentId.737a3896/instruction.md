# Bug Report

### Describe the bug

I'm experiencing an issue where `getByParentId()` is not returning all API specs for a given workspace. It seems like the function is only returning the first matching spec instead of all specs that belong to the workspace.

### Reproduction

```js
// Create multiple API specs for the same workspace
const workspaceId = 'workspace_123';

// Add spec 1
await createApiSpec({ parentId: workspaceId, name: 'Spec 1' });

// Add spec 2
await createApiSpec({ parentId: workspaceId, name: 'Spec 2' });

// Add spec 3
await createApiSpec({ parentId: workspaceId, name: 'Spec 3' });

// Try to retrieve all specs
const specs = getByParentId(workspaceId);

console.log(specs.length); // Expected: 3, Actual: 1
```

### Expected behavior

`getByParentId()` should return an array containing all API specs that have the matching `parentId`. If a workspace has 3 specs associated with it, all 3 should be returned.

### Actual behavior

Only the first matching spec is returned, even when multiple specs exist for the same workspace. The other specs are ignored.

This is causing issues in the UI where only one spec shows up per workspace instead of displaying all available specs.

---
Repository: /testbed
