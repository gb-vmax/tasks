# Bug Report

### Describe the bug

The `database.duplicate()` function appears to be broken after a recent change. When trying to duplicate documents, the operation fails or produces incomplete results. The duplication process seems to cut off mid-execution.

### Reproduction

```js
const originalDoc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  parentId: 'wrk_456'
};

// Try to duplicate the document
const duplicated = await database.duplicate(originalDoc);
// This fails or returns an incomplete/malformed document
```

### Expected behavior

The `duplicate()` function should successfully create a complete copy of the document with a new ID and updated timestamps. All properties should be properly copied over and any child documents should also be duplicated recursively.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might have been introduced in a recent refactor. The function was working fine before but now it's not completing the duplication process properly.

---
Repository: /testbed
