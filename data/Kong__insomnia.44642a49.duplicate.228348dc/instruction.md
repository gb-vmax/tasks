# Bug Report

### Describe the bug

When duplicating documents with the `database.duplicate()` function, the naming behavior has changed unexpectedly. Previously, duplicated documents would retain their original names, but now they're being automatically renamed with a "(Copy)" suffix pattern.

### Reproduction

```js
const originalDoc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My API Request',
  parentId: 'fld_456'
};

const duplicated = await database.duplicate(originalDoc);

// Expected: duplicated.name === 'My API Request'
// Actual: duplicated.name === 'My API Request (Copy)'
```

If you duplicate the same document multiple times, it increments:
- First duplicate: "My API Request (Copy)"
- Second duplicate: "My API Request (Copy 2)"
- Third duplicate: "My API Request (Copy 3)"

### Expected behavior

The duplicate function should preserve the original document's name unless explicitly overridden via the `patch` parameter. The automatic renaming with "(Copy)" suffix is interfering with our workflow where we need exact duplicates.

### Additional context

This seems to have started happening recently. We rely on being able to create exact copies of requests and then manually rename them as needed. The automatic renaming is breaking our automation scripts that expect duplicates to have the same name as the original.

---
Repository: /testbed
