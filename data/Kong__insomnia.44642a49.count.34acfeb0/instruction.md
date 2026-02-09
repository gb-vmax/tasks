# Bug Report

### Describe the bug

I'm experiencing an issue with the database count function where it's returning incorrect values. When I query the database to count documents, I'm getting a count that's off by one - it's always returning one more than the actual number of documents.

### Reproduction

```js
// Create some documents in the database
await database.docCreate('request', { name: 'Request 1' });
await database.docCreate('request', { name: 'Request 2' });

// Count the documents
const count = await database.count('request', {});
console.log(count); // Expected: 2, but getting: 3
```

The count is consistently one higher than expected across different document types. This is causing issues in our UI where pagination and document counts are displayed incorrectly.

### Expected behavior

The `count` function should return the exact number of documents matching the query, not an inflated value.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
