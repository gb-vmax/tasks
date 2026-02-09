# Bug Report

### Describe the bug

The `database.all()` function is returning incorrect results when the database is not empty. It seems like the function logic got inverted - when `db._empty` is false (meaning the database has data), it's using the wrong code path.

### Reproduction

```js
// Assume database has some data
db._empty = false;

// Try to fetch all documents of a type
const results = await database.all('request');

// Expected: Should use _send to fetch from the database
// Actual: Falls back to database.find() instead
```

### Steps to reproduce
1. Initialize a database with some documents
2. Call `database.all()` with a document type
3. The function uses `database.find()` instead of properly calling `_send()`

### Expected behavior

When the database is **not** empty (`db._empty === false`), the function should call `_send()` to fetch all documents. When the database **is** empty (`db._empty === true`), it should fall back to `database.find()`.

Currently it appears to be doing the opposite.

### Additional context

This is causing issues with data retrieval in non-empty databases. The conditional check seems backwards.

---
Repository: /testbed
