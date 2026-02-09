# Bug Report

### Describe the bug

I'm experiencing an issue with the `database.find()` function where it's not returning all the expected results. When querying the database, the first item in the result set is consistently missing from the returned array.

### Reproduction

```js
// Insert multiple documents
await database.insert(modelType, { name: 'Item 1', created: 1000 });
await database.insert(modelType, { name: 'Item 2', created: 2000 });
await database.insert(modelType, { name: 'Item 3', created: 3000 });

// Query all documents
const results = await database.find(modelType, {});

// Expected: 3 items
// Actual: 2 items (first item is missing)
console.log(results.length); // outputs 2 instead of 3
```

### Expected behavior

The `find()` method should return all documents that match the query. If I insert 3 documents and query with an empty filter, I should get all 3 documents back.

### Additional context

This seems to have started happening recently. The sorting behavior also appears to be reversed - items are coming back in the opposite order than before (newest first instead of oldest first when using the default sort).

---
Repository: /testbed
