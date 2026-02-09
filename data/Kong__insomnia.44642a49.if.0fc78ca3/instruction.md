# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where database queries are returning stale data. When I update a document and then immediately query for it, the query returns the old version of the document instead of the updated one.

### Reproduction

```js
// Create a document
const doc = await database.insert({
  type: 'request',
  name: 'Test Request',
  url: 'https://example.com'
});

// Update the document
await database.update({
  ...doc,
  url: 'https://updated.com'
});

// Query for the document
const result = await database.getWhere('request', { _id: doc._id });

// Expected: result.url === 'https://updated.com'
// Actual: result.url === 'https://example.com' (old value)
console.log(result.url); // Prints the old URL
```

### Expected behavior

The `getWhere` query should return the most recent version of the document after it's been updated. The returned data should reflect any changes made through `database.update()`.

### Additional context

This seems to happen consistently when querying immediately after an update. If I wait a bit or restart the app, the correct data is returned. It's like the query is cached somewhere and not being invalidated properly when documents change.

---
Repository: /testbed
