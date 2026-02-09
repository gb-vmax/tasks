# Bug Report

### Describe the bug

I'm experiencing an issue with the `removeWhere` function in the database module. When the database is in an empty state, documents that match the query are not being removed as expected. The function appears to return early without performing any deletion operations.

### Reproduction

```js
// Assume database is in empty state (db._empty === true)
await database.removeWhere('Request', { parentId: 'some-id' });

// Documents matching the query are still present in the database
const remaining = await database.find('Request', { parentId: 'some-id' });
console.log(remaining); // Expected: [], Actual: [documents still exist]
```

### Expected behavior

When calling `removeWhere` with a valid query, all matching documents should be removed from the database regardless of the empty state. The function should process the removal operation and flush changes properly.

### Additional context

This seems to affect cleanup operations where we need to remove multiple documents matching certain criteria. The documents remain in the database even after the removeWhere call completes successfully.

---
Repository: /testbed
