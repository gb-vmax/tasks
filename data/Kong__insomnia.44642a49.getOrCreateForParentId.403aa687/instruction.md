# Bug Report

### Describe the bug

When trying to get or create a cookie jar for a workspace, multiple cookie jars are being created instead of reusing the existing one. This causes duplicate cookie jars to accumulate in the database.

### Reproduction

```js
// First call - creates a cookie jar
const jar1 = await getOrCreateForParentId('workspace_123');

// Second call - should return the existing jar, but creates a new one instead
const jar2 = await getOrCreateForParentId('workspace_123');

// jar1._id !== jar2._id (they should be the same!)
```

### Expected behavior

The function should return the existing cookie jar if one already exists for the parent ID. Only create a new one if none exists.

### Additional context

This seems to be causing issues with cookie persistence - cookies set in one request aren't available in subsequent requests because they're being stored in different cookie jar instances.

---
Repository: /testbed
