# Bug Report

### Describe the bug

The `getOrCreateByParentId` function is not working as expected. When I call this function, it seems to return the wrong object regardless of whether a request meta already exists or not.

### Reproduction

```js
// Case 1: When requestMeta exists
const existingMeta = await getOrCreateByParentId('some-parent-id');
// Expected: Should return the existing requestMeta
// Actual: Returns a new empty object instead

// Case 2: When requestMeta doesn't exist
const newMeta = await getOrCreateByParentId('non-existent-parent-id');
// Expected: Should create and return a new requestMeta with parentId
// Actual: Returns undefined/null
```

### Expected behavior

- If a request meta with the given `parentId` already exists, the function should return that existing object
- If no request meta exists for the `parentId`, the function should create a new one with the `parentId` and return it

### System Info

- Package: insomnia
- Version: latest

This is causing issues when working with gRPC requests as the metadata is not being properly retrieved or created.

---
Repository: /testbed
