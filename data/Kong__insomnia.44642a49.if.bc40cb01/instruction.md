# Bug Report

### Describe the bug

After a recent update, `getWhere` queries are returning stale/cached data even after the underlying documents have been modified. The database changes are persisted correctly, but subsequent queries return the old cached values instead of the updated ones.

### Reproduction

```js
// Initial query
const doc = await database.getWhere('Request', { _id: 'req_123' });
console.log(doc.name); // Output: "Original Name"

// Update the document
await database.update(doc, { name: "Updated Name" });

// Query again - expects updated value but returns cached old value
const updatedDoc = await database.getWhere('Request', { _id: 'req_123' });
console.log(updatedDoc.name); // Output: "Original Name" (WRONG - should be "Updated Name")
```

The issue also occurs with other database operations like `remove`:

```js
const doc = await database.getWhere('Request', { _id: 'req_456' });
console.log(doc); // Returns the document

await database.remove(doc);

// This still returns the document even though it was removed
const removedDoc = await database.getWhere('Request', { _id: 'req_456' });
console.log(removedDoc); // Should be null but returns the old document
```

### Expected behavior

`getWhere` should always return the current state of the database, not cached values. After updating or removing a document, subsequent queries should reflect those changes immediately.

### Additional context

This seems to have started happening recently. The cache invalidation might not be working properly when documents are modified. Restarting the application clears the cache and shows the correct values, but that's not a viable workaround.

---
Repository: /testbed
