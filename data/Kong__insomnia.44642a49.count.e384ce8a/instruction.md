# Bug Report

### Describe the bug

After a recent update, I'm noticing that count queries are returning stale/cached results even after documents are modified or deleted. The count doesn't update immediately to reflect the actual state of the database.

### Reproduction

```js
// Create some documents
await database.insert({ type: 'request', name: 'Test 1' });
await database.insert({ type: 'request', name: 'Test 2' });

// Count returns 2 (correct)
const count1 = await database.count('request');
console.log(count1); // 2

// Delete one document
await database.remove({ type: 'request', name: 'Test 1' });

// Count still returns 2 (incorrect - should be 1)
const count2 = await database.count('request');
console.log(count2); // 2 (expected: 1)
```

The count query is returning cached data instead of querying the actual database state. This happens immediately after modifying/deleting documents.

### Expected behavior

The `count()` method should return the current number of documents in the database, reflecting any recent changes like inserts, updates, or deletes.

### Additional context

This seems to have started happening recently. The counts eventually become correct after waiting a few seconds, but they should be accurate immediately after database operations.

---
Repository: /testbed
