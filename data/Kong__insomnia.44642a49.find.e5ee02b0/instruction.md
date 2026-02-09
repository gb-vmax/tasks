# Bug Report

### Describe the bug

The `database.find()` method is not respecting the sort order passed as a parameter. When querying documents with a custom sort order, the results are returned in an unexpected order instead of the specified sort criteria.

### Reproduction

```js
// Query with custom sort order
const docs = await database.find('requests', {}, { name: 1 });

// Expected: Documents sorted by name in ascending order
// Actual: Documents returned in reverse order, ignoring the sort parameter
```

### Steps to reproduce
1. Call `database.find()` with a specific sort parameter (e.g., `{ name: 1 }` or `{ modified: -1 }`)
2. Observe that the returned documents don't follow the specified sort order
3. The results appear to be in reverse order regardless of what sort criteria is provided

### Expected behavior

The documents should be sorted according to the `sort` parameter passed to the function. For example, if `{ created: 1 }` is passed, documents should be sorted by creation date in ascending order.

### Additional context

This affects all database queries that rely on custom sorting, making it difficult to retrieve documents in the correct order for display or processing.

---
Repository: /testbed
