# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database queries not returning the most up-to-date data. When I update a document and immediately query for it, sometimes I get stale data instead of the latest values.

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

// Expected: url should be 'https://updated.com'
// Actual: url is still 'https://example.com'
console.log(result.url); // prints old value
```

### Expected behavior

Queries should always return the most recent version of documents. After updating a document, subsequent queries should reflect those changes immediately.

### Additional context

This seems to happen intermittently, especially when queries are made in quick succession after updates. Sometimes the data is correct, other times it returns outdated values. This is causing issues in our workflow where we need to update and then immediately read back documents.

System: Insomnia latest version

---
Repository: /testbed
