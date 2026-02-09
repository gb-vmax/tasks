# Bug Report

### Describe the bug

The database `count()` method is returning incorrect values when querying documents. It appears to always return `0` even when documents matching the query exist in the database.

### Reproduction

```js
// Create some documents
await database.docCreate('Request', { name: 'Test Request 1' });
await database.docCreate('Request', { name: 'Test Request 2' });

// Try to count them
const count = await database.count('Request', {});
console.log(count); // Expected: 2, Actual: 0
```

The count method returns 0 regardless of how many documents are actually in the database. This is breaking functionality that relies on checking document counts before performing operations.

### Expected behavior

The `count()` method should return the actual number of documents matching the query. If no query is provided, it should return the total count of documents of that type.

### Additional context

This seems to have started happening recently. The method worked correctly before and now it's consistently returning 0 for all queries, even when I can verify the documents exist using other database methods.

---
Repository: /testbed
