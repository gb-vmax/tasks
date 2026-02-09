# Bug Report

### Describe the bug

When calling `database.withAncestors()` with an empty database, the function returns an empty array instead of properly delegating to the `_send` method. This causes issues when trying to retrieve ancestor documents in scenarios where the database is in an empty state but should still communicate with the underlying data layer.

### Reproduction

```js
// Simulate empty database state
db._empty = true;

// Try to get ancestors for a document
const doc = { _id: 'test', type: 'request' };
const ancestors = await database.withAncestors(doc, ['workspace']);

// Expected: Should call _send('withAncestors', ...) and return proper result
// Actual: Returns empty array []
```

### Expected behavior

The `withAncestors` function should delegate to `_send('withAncestors', ...)` when the database is in an empty state, allowing the underlying communication layer to handle the request appropriately. It should only return an empty array when the document itself is null/undefined.

### Additional context

This seems to have broken the ability to fetch ancestor hierarchies when working with an empty local database cache that needs to query the remote data source. The function now short-circuits and returns `[]` immediately instead of forwarding the request.

---
Repository: /testbed
