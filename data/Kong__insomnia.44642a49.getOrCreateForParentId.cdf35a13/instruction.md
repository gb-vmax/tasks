# Bug Report

### Describe the bug

When calling `getOrCreateForParentId()` for a workspace that already has a cookie jar, the function creates a new cookie jar instead of returning the existing one. This leads to duplicate cookie jars being created for the same parent workspace.

### Reproduction

```js
// First call - creates a cookie jar
const jar1 = await getOrCreateForParentId('workspace_123');

// Second call - should return jar1 but creates a new one instead
const jar2 = await getOrCreateForParentId('workspace_123');

// jar1 and jar2 are different objects when they should be the same
console.log(jar1._id === jar2._id); // false (but should be true)
```

### Expected behavior

The function should return the existing cookie jar if one already exists for the given `parentId`, and only create a new one if none exists. Multiple calls with the same `parentId` should always return the same cookie jar instance.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with cookie management across the application since each call creates a new jar instead of reusing the existing one.

---
Repository: /testbed
