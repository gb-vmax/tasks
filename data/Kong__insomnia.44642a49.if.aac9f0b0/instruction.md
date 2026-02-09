# Bug Report

### Describe the bug

When calling `removeWhere()` on the database, documents are not being removed as expected. The method appears to return early without actually performing the removal operation, leaving the documents in the database.

### Reproduction

```js
// Add some documents to the database
await database.insert(model, { _id: 'doc1', name: 'test1' });
await database.insert(model, { _id: 'doc2', name: 'test2' });

// Try to remove documents matching a query
await database.removeWhere('model', { name: 'test1' });

// The document is still present in the database
const remaining = await database.find('model', {});
console.log(remaining); // Expected: [{ _id: 'doc2', name: 'test2' }]
                        // Actual: [{ _id: 'doc1', name: 'test1' }, { _id: 'doc2', name: 'test2' }]
```

### Expected behavior

The `removeWhere()` method should remove all documents matching the provided query from the database. Documents that don't match the query should remain.

### Additional context

This seems to affect all calls to `removeWhere()` regardless of the query parameters. The documents are never actually removed from the database.

---
Repository: /testbed
