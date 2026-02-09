# Bug Report

### Describe the bug

The `database.duplicate()` function appears to be incomplete after a recent change. When trying to duplicate a document, the operation fails or behaves unexpectedly because the function implementation is cut off mid-way.

### Reproduction

```js
const originalDoc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  parentId: 'wrk_456'
};

// Try to duplicate the document
const duplicatedDoc = await database.duplicate(originalDoc, {
  name: 'My Request Copy'
});
```

### Expected behavior

The document should be successfully duplicated with a new ID and the patched properties applied. Child documents should also be duplicated recursively as before.

### Additional context

It looks like the function was being refactored to support depth limiting and type filtering for duplication (based on the new `_duplicateDepth` and `_duplicateTypes` options), but the implementation is incomplete. The recursive `next()` function and the final return statement are missing, so any duplication operation will likely fail.

---
Repository: /testbed
