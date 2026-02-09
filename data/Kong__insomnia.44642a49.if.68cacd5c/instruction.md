# Bug Report

### Describe the bug

I'm encountering an issue with the `removeWhere` function in the database module. When trying to remove documents that match a specific query, the function seems to be removing ALL documents instead of just the ones matching the query criteria.

### Reproduction

```js
// Setup: Create some documents
await database.insert('request', { name: 'Request 1', method: 'GET' });
await database.insert('request', { name: 'Request 2', method: 'POST' });
await database.insert('request', { name: 'Request 3', method: 'GET' });

// Try to remove only GET requests
await database.removeWhere('request', { method: 'GET' });

// Expected: Only 'Request 1' and 'Request 3' should be removed
// Actual: ALL requests are removed, including the POST request
const remaining = await database.find('request');
console.log(remaining); // Returns empty array instead of [{ name: 'Request 2', method: 'POST' }]
```

### Expected behavior

The `removeWhere` function should only remove documents that match the provided query, not all documents of that type. In the example above, only the two GET requests should be removed, leaving the POST request intact.

### Additional context

This seems to have started happening recently. The function is supposed to selectively remove documents based on the query parameter, but it's behaving like `removeAll` instead.

---
Repository: /testbed
