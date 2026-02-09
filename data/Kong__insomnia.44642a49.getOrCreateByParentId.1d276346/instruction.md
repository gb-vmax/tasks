# Bug Report

### Describe the bug

The `getOrCreateByParentId` function is not working as expected. When a workspace meta document already exists for a given `parentId`, the function still creates a new document instead of returning the existing one.

### Reproduction

```js
// First call - creates a new workspace meta
const meta1 = await getOrCreateByParentId('workspace_123');

// Second call - should return the existing meta, but creates a new one instead
const meta2 = await getOrCreateByParentId('workspace_123');

// meta1 and meta2 should be the same document, but they're different
console.log(meta1._id === meta2._id); // Expected: true, Actual: false
```

### Expected behavior

When a workspace meta document already exists for the given `parentId`, the function should return the existing document instead of creating a duplicate. The function should only create a new document when one doesn't exist yet.

### Additional context

This seems to have started happening recently. The function name suggests it should "get or create" the document, but currently it's always creating new documents even when they already exist.

---
Repository: /testbed
