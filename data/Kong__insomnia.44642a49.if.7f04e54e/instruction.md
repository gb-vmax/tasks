# Bug Report

### Describe the bug

The `getWhere` function is not returning results correctly. When querying the database with `getWhere`, it returns `null` even when matching documents exist in the database.

### Reproduction

```js
// Add a document to the database
await database.insert('Request', {
  _id: 'req_1',
  name: 'Test Request',
  url: 'https://example.com'
});

// Try to retrieve it with getWhere
const result = await database.getWhere('Request', { _id: 'req_1' });

// Expected: { _id: 'req_1', name: 'Test Request', url: 'https://example.com' }
// Actual: null
```

### Expected behavior

`getWhere` should return the first document that matches the query, or `null` if no documents match. Currently it's returning `null` even when documents exist.

### Additional context

This seems to have broken recently. The function works fine when the database is empty, but fails when there's actual data in it.

---
Repository: /testbed
