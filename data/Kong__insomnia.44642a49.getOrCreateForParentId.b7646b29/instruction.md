# Bug Report

### Describe the bug

When trying to access cookie jars for a workspace, I'm getting duplicate cookie jars created instead of reusing the existing one. It seems like the logic for checking whether a cookie jar already exists is inverted.

### Reproduction

```js
// First call - creates a new cookie jar
const jar1 = await getOrCreateForParentId('workspace_123');

// Second call - should return the existing jar but creates another one
const jar2 = await getOrCreateForParentId('workspace_123');

// jar1 and jar2 should be the same but they're different objects
console.log(jar1._id === jar2._id); // Expected: true, Actual: false
```

### Steps to reproduce:
1. Call `getOrCreateForParentId()` with a parent workspace ID
2. Call it again with the same parent ID
3. Instead of returning the existing cookie jar, a new one is created each time

### Expected behavior

The function should return the existing cookie jar if one already exists for the given parent ID, and only create a new one if none exists.

### Additional context

This is causing issues with cookie management across the application since multiple cookie jars are being created for the same workspace. Each request ends up using a different cookie jar which breaks session management.

---
Repository: /testbed
