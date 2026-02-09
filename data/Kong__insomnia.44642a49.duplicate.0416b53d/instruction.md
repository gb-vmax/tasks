# Bug Report

### Describe the bug

When duplicating documents in the database, the duplicate operation is creating items with names that conflict with existing siblings. The function should be generating unique names like "Item (Copy)", "Item (Copy 2)", etc., but instead it seems to be using the original name or not properly checking for conflicts.

### Reproduction

```js
// Create a parent document
const parent = await database.insert({
  _id: 'parent_1',
  type: 'folder',
  name: 'My Folder',
  parentId: null
});

// Create a child document
const originalDoc = await database.insert({
  _id: 'doc_1',
  type: 'request',
  name: 'Test Request',
  parentId: 'parent_1'
});

// Duplicate the document
const duplicated = await database.duplicate(originalDoc);

// Expected: duplicated.name should be "Test Request (Copy)"
// Actual: duplicated.name is "Test Request" (same as original)
```

### Expected behavior

When duplicating a document without providing a custom name in the patch, the duplicate should automatically get a unique name by appending "(Copy)" or "(Copy N)" where N is incremented until a unique name is found among siblings with the same parent.

### Additional context

This seems to have broken recently. The duplicate function should be checking sibling documents to ensure name uniqueness, but it's not working as expected.

---
Repository: /testbed
