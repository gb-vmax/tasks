# Bug Report

### Describe the bug

When querying the database using `find()`, the first result is missing from the returned array. All subsequent results are returned correctly, but the first item is consistently skipped.

### Reproduction

```js
// Create some test documents
await database.insert(models.request.type, { name: 'Request 1' });
await database.insert(models.request.type, { name: 'Request 2' });
await database.insert(models.request.type, { name: 'Request 3' });

// Query all documents
const results = await database.find(models.request.type, {});

console.log(results.length); // Expected: 3, Actual: 2
console.log(results[0].name); // Expected: 'Request 1', Actual: 'Request 2'
```

### Expected behavior

The `find()` method should return all matching documents, including the first one. In the example above, all three requests should be returned in the results array.

### Additional context

This seems to affect all queries regardless of the query parameters or sort order. The first document in the result set is always missing.

---
Repository: /testbed
