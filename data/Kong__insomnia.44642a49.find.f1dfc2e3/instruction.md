# Bug Report

### Describe the bug

I'm experiencing an issue with the `database.find()` function where it only returns a single document instead of all matching documents. When querying for multiple records, the function returns an array with just the first result, even though there are multiple documents that match the query criteria.

### Reproduction

```js
// Insert multiple documents
await database.insert('request', { name: 'Request 1', created: 1000 });
await database.insert('request', { name: 'Request 2', created: 2000 });
await database.insert('request', { name: 'Request 3', created: 3000 });

// Try to find all requests
const requests = await database.find('request', {});

// Expected: Array with 3 requests
// Actual: Array with only 1 request (the first one)
console.log(requests.length); // Prints 1 instead of 3
```

### Expected behavior

The `find()` method should return all documents that match the query, not just the first one. In the example above, it should return an array containing all 3 request documents.

### Additional context

This seems to have broken recently. The function used to work correctly and return all matching documents. Now it's cutting off after the first result.

---
Repository: /testbed
