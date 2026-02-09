# Bug Report

### Describe the bug

The `database.find()` function is returning incomplete results - it's missing the first document from the query results. When querying for multiple documents, only the second document onwards are being returned.

### Reproduction

```js
// Create multiple documents of the same type
await database.insert({ type: 'request', name: 'Request 1' });
await database.insert({ type: 'request', name: 'Request 2' });
await database.insert({ type: 'request', name: 'Request 3' });

// Query for all requests
const requests = await database.find('request');

// Expected: 3 documents
// Actual: 2 documents (missing the first one)
console.log(requests.length); // Shows 2 instead of 3
console.log(requests[0].name); // Shows "Request 2" instead of "Request 1"
```

### Expected behavior

The `find()` method should return all documents that match the query, including the first document in the result set.

### Additional context

This seems to affect all queries regardless of the document type or query parameters. The first document is consistently missing from the results.

---
Repository: /testbed
