# Bug Report

### Describe the bug

I'm experiencing an issue with the `removeWhere` function in the database module. When the database is not empty, the function appears to return early without actually removing any documents. This means that documents matching the query are not being deleted as expected.

### Reproduction

```js
// Assuming database is initialized and not empty
await database.insert(someType, {
  _id: 'test-doc',
  name: 'Test Document'
});

// Try to remove the document
await database.removeWhere(someType, { _id: 'test-doc' });

// Document still exists in the database
const doc = await database.getWhere(someType, { _id: 'test-doc' });
console.log(doc); // Still returns the document instead of null/undefined
```

### Expected behavior

When calling `removeWhere` with a valid query, all matching documents should be removed from the database regardless of whether the database is empty or not. The function should only take the early return path when the database IS empty, not when it's populated with data.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
