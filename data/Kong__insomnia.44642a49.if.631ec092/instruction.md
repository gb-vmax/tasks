# Bug Report

### Describe the bug

I'm experiencing an issue where database queries are returning stale/cached data after recent changes. When I update a document and then immediately query for it using `getWhere`, the old version of the document is returned instead of the updated one.

### Reproduction

```js
// Create or update a document
await database.update(doc, { name: 'Updated Name' });

// Immediately query for the same document
const result = await database.getWhere('MyType', { _id: doc._id });

// result.name still shows the old value instead of 'Updated Name'
console.log(result.name); // Expected: 'Updated Name', Actual: old value
```

### Steps to reproduce:
1. Query a document using `getWhere`
2. Update that document using `database.update` or similar method
3. Query the same document again with `getWhere` using the same query parameters
4. The returned document contains old data instead of the updated values

This seems to happen consistently when querying within a short time window after updates. If I wait a bit longer (maybe half a second or so?), it eventually returns the correct data.

### Expected behavior

`getWhere` should always return the most up-to-date version of documents from the database, especially right after updates are made. Queries should reflect the current state of the data, not cached/stale versions.

### Additional context

This started happening recently and is causing issues in our application where we need to verify that updates were applied correctly. The cached data is causing validation checks to fail because they're comparing against outdated values.

---
Repository: /testbed
