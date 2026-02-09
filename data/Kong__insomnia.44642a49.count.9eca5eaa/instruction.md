# Bug Report

### Describe the bug

I'm experiencing an issue where database count queries are returning stale/cached results after documents are modified. When I update or delete documents, subsequent count queries still return the old count values instead of reflecting the actual current state of the database.

### Reproduction

```js
// Create some documents
await database.insert({ type: 'Request', name: 'Test 1' });
await database.insert({ type: 'Request', name: 'Test 2' });

// Count returns 2 (correct)
const count1 = await database.count('Request', {});
console.log(count1); // 2

// Delete one document
await database.remove({ type: 'Request', name: 'Test 1' });

// Count still returns 2 (incorrect - should be 1)
const count2 = await database.count('Request', {});
console.log(count2); // Expected: 1, Actual: 2
```

The same issue occurs with updates:

```js
await database.insert({ type: 'Request', status: 'active' });
await database.insert({ type: 'Request', status: 'active' });

const count1 = await database.count('Request', { status: 'active' });
console.log(count1); // 2

// Update one document
await database.update({ type: 'Request', status: 'active' }, { status: 'inactive' });

// Count query with filter returns stale result
const count2 = await database.count('Request', { status: 'active' });
console.log(count2); // Expected: 1, Actual: 2
```

### Expected behavior

Count queries should always return the current/accurate count of documents matching the query, especially after insert, update, or delete operations.

### System Info
- Version: Latest
- Platform: All platforms affected

This seems to have started happening recently. The counts eventually update after some time, but they should be accurate immediately after changes are made to the database.

---
Repository: /testbed
