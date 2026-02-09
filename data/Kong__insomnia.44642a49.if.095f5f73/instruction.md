# Bug Report

### Describe the bug

The `getWhere` function is not returning any results when querying the database. It seems like queries that should return a single document are returning `null` instead, even when matching documents exist in the database.

### Reproduction

```js
// Assuming we have a document in the database
await database.insert('Request', {
  _id: 'req_1',
  name: 'Test Request',
  parentId: 'wrk_1'
});

// This returns null even though the document exists
const result = await database.getWhere('Request', { 
  parentId: 'wrk_1' 
});

console.log(result); // Expected: document object, Actual: null
```

### Expected behavior

`getWhere` should return the first matching document when the query matches existing documents in the database. Currently it's returning `null` for all queries.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
