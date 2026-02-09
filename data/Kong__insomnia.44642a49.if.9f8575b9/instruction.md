# Bug Report

### Describe the bug

When trying to update existing documents in the database, the operation fails silently or behaves unexpectedly. It seems like documents aren't being updated properly even though the update function is called correctly.

### Reproduction

```js
// Create a document first
const doc = await database.insert({
  _id: 'test-doc',
  name: 'Original Name',
  type: 'workspace'
});

// Try to update the document
const updated = await database.update({
  ...doc,
  name: 'Updated Name'
});

// The document doesn't reflect the changes
console.log(updated.name); // Expected: 'Updated Name', but changes aren't persisted
```

### Expected behavior

The `database.update()` function should properly update existing documents in the database. The updated values should be persisted and returned correctly.

### Additional context

This seems to have started happening recently. The update method is being called but the documents aren't actually being updated in the underlying database. Not sure if this is related to the sync functionality or something else.

---
Repository: /testbed
