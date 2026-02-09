# Bug Report

### Describe the bug

The `database.getWhere()` function is returning incorrect results when the database is not empty. It appears that the function is bypassing the remote database call and falling through to the local find operation when it shouldn't.

### Reproduction

```js
// Assuming db is not empty
const result = await database.getWhere('Request', { _id: 'req_123' });

// Expected: Should query the remote database via _send
// Actual: Falls through to local database.find() instead
```

### Steps to reproduce:
1. Initialize database with some data (db._empty = false)
2. Call `database.getWhere()` with a valid type and query
3. The function incorrectly uses the local find operation instead of sending to remote database

### Expected behavior

When the database is not empty, `getWhere()` should delegate to the remote database via `_send()`. The local fallback should only be used when the database IS empty.

### Additional context

This seems to be affecting query results when working with a populated database. The logic for when to use remote vs local database appears to be inverted.

---
Repository: /testbed
