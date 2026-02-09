# Bug Report

### Describe the bug

The `getMostRecentlyModified` function is returning incorrect results. When the database is not empty, it appears to be fetching recently created items instead of recently modified ones.

### Reproduction

```js
// Create some documents
const doc1 = await database.insert('Request', { name: 'First', modified: 1000 });
const doc2 = await database.insert('Request', { name: 'Second', modified: 2000 });

// Update doc1 to have the most recent modification time
await database.update(doc1, { modified: 3000 });

// This should return doc1 (most recently modified)
// But it returns doc2 instead
const result = await database.getMostRecentlyModified('Request');
console.log(result.name); // Expected: 'First', Actual: 'Second'
```

### Expected behavior

`getMostRecentlyModified` should return the document with the most recent modification timestamp, not the most recently created document.

### Additional context

This seems to be affecting workflows where we need to retrieve the last modified item from the database. The function is returning items based on creation time rather than modification time.

---
Repository: /testbed
