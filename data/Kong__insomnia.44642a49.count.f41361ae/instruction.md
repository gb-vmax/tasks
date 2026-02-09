# Bug Report

### Describe the bug

I'm experiencing an issue with the database count function. When querying the database to count documents, I'm getting a count of 0 returned even when there are matching documents in the collection.

### Reproduction

```js
// Add some documents to the database
await database.docCreate('request', { name: 'Test Request 1' });
await database.docCreate('request', { name: 'Test Request 2' });

// Try to count all requests
const count = await database.count('request', {});
console.log(count); // Expected: 2, Actual: 0
```

The count always returns 0 regardless of how many documents actually exist in the collection. This seems to happen after a recent update.

### Expected behavior

The `count` function should return the actual number of documents matching the query. In the example above, it should return 2 since we created 2 request documents.

### Additional context

This is blocking our ability to implement pagination and show accurate counts in the UI. The documents are being created successfully (we can retrieve them with other queries), but the count function specifically is not working as expected.

---
Repository: /testbed
