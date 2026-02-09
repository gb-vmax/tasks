# Bug Report

### Describe the bug

When duplicating documents with the `duplicate()` function, the patch parameter is being ignored and the duplicated document doesn't reflect the changes specified in the patch.

### Reproduction

```js
const originalDoc = {
  _id: 'req_123',
  type: 'Request',
  name: 'Original Request',
  method: 'GET',
  parentId: 'wrk_1'
};

const patch = {
  name: 'Duplicated Request',
  method: 'POST'
};

const duplicatedDoc = await database.duplicate(originalDoc, patch);

// Expected: duplicatedDoc.name = 'Duplicated Request', duplicatedDoc.method = 'POST'
// Actual: duplicatedDoc.name = 'Original Request', duplicatedDoc.method = 'GET'
```

### Expected behavior

The duplicated document should have the properties from the patch applied. When passing a patch object to `duplicate()`, those properties should override the original document's properties in the new copy.

For example, if I duplicate a request and want to change its name or method, the patch should be applied to the duplicate, not ignored.

### Additional context

This also affects child documents when duplicating hierarchical structures. When duplicating a folder with requests inside, if you pass a patch to update the parent folder's properties, those changes should be reflected in the duplicate.

---
Repository: /testbed
