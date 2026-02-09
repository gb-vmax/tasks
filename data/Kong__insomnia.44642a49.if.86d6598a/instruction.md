# Bug Report

### Describe the bug

After a recent update, the database query system seems to be returning stale data. When I update a document and immediately query for it using `getWhere()`, I'm getting the old version of the document instead of the updated one.

### Reproduction

```js
// Create a document
const doc = await database.insert({
  type: 'Request',
  name: 'Test Request',
  url: 'https://example.com'
});

// Update the document
await database.update({
  ...doc,
  url: 'https://updated.com'
});

// Query for the document
const result = await database.getWhere('Request', { _id: doc._id });

// Result still shows the old URL: 'https://example.com'
// Expected: 'https://updated.com'
```

### Expected behavior

The `getWhere()` method should always return the most current version of documents from the database, not cached or stale data.

### Additional context

This seems to happen consistently when:
1. Creating or updating a document
2. Immediately querying for it with `getWhere()`
3. The query returns outdated data

Sometimes waiting a bit before querying returns the correct data, which makes me think there might be some caching involved that's not being invalidated properly.

---
Repository: /testbed
