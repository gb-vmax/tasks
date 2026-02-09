# Bug Report

### Describe the bug

After a recent update, database queries are returning stale/cached data even after documents have been modified. When I update a document and immediately query for it, I'm getting the old version instead of the updated one.

### Reproduction

```js
// Create a document
const doc = await database.insert({
  type: 'request',
  name: 'Test Request',
  url: 'https://example.com'
});

// Update the document
await database.update(doc, { name: 'Updated Request' });

// Query for the document
const results = await database.find('request', { _id: doc._id });

// Expected: results[0].name === 'Updated Request'
// Actual: results[0].name === 'Test Request' (old value)
```

The same issue happens with other operations too:

1. Insert a new document
2. Query with `find()` - works fine
3. Delete or update the document
4. Query again with the same parameters
5. Still get the old results

This is really problematic for workflows where we need to see changes immediately after making them. It seems like queries are being cached but the cache isn't being invalidated when data changes.

### Expected behavior

`database.find()` should always return the current state of the database, not cached results from previous queries.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
