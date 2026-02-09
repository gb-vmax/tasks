# Bug Report

### Describe the bug

I'm experiencing an issue with the `database.find()` function where it's not returning all the documents from the query results. It seems like the first document in the result set is being skipped/missing.

### Reproduction

```js
// Create some test documents
await database.insert(type, { name: 'doc1', created: 1 });
await database.insert(type, { name: 'doc2', created: 2 });
await database.insert(type, { name: 'doc3', created: 3 });

// Query all documents
const results = await database.find(type, {});

// Expected: 3 documents
// Actual: Only 2 documents returned (missing the first one)
console.log(results.length); // Shows 2 instead of 3
```

### Expected behavior

The `find()` method should return all documents that match the query. In the example above, all 3 documents should be returned, but only 2 are being returned.

### Additional context

This appears to be happening consistently - the first document in the result set is always missing from the returned array. Not sure if this is related to a recent change, but it's causing issues in our application where we're expecting complete result sets.

---
Repository: /testbed
