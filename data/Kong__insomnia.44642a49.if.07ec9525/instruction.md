# Bug Report

### Describe the bug

The `removeWhere` function is not working correctly when the database is not empty. It appears that documents matching the query are not being removed as expected.

### Reproduction

```js
// Assuming db is not empty
await database.removeWhere('Request', { 
  parentId: 'some-parent-id' 
});

// Documents are still present in the database
const docs = await database.find('Request', { 
  parentId: 'some-parent-id' 
});
console.log(docs.length); // Expected: 0, Actual: > 0
```

### Expected behavior

When calling `removeWhere` with a type and query, all documents matching that query should be removed from the database, regardless of whether the database is empty or not.

### Additional context

This seems to affect the normal operation when the database has existing data. The removal logic doesn't appear to execute when it should.

---
Repository: /testbed
