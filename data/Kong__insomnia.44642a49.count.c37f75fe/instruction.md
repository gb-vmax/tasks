# Bug Report

### Describe the bug
The `database.count()` function is returning incorrect counts - it's off by one and returns a value that's 1 less than the actual number of documents in the collection.

### Reproduction
```js
// Create some documents
await database.docCreate('Request', { name: 'Request 1' });
await database.docCreate('Request', { name: 'Request 2' });
await database.docCreate('Request', { name: 'Request 3' });

// Try to count them
const count = await database.count('Request', {});
console.log(count); // Expected: 3, Actual: 2
```

### Expected behavior
`database.count()` should return the exact number of documents matching the query. If there are 3 documents, it should return 3, not 2.

### Additional context
This seems to have started recently. The count is consistently off by one for any query I run. Not sure if this is related to the buffer changes or something else, but it's affecting my ability to implement pagination correctly.

---
Repository: /testbed
