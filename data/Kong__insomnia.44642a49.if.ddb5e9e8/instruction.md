# Bug Report

### Describe the bug

I'm experiencing an issue with the database query function `getWhere()`. When the database is not empty, the function returns the wrong result or fails to execute properly. It seems like the logic for checking whether the database is empty got inverted somehow.

### Reproduction

```js
// Assuming database has some documents
const result = await database.getWhere('Request', { _id: 'req_123' });

// Expected: Should return the document or null if not found
// Actual: Returns undefined or throws an error
```

### Steps to reproduce:
1. Initialize database with some documents
2. Call `getWhere()` with a valid type and query
3. The function doesn't return the expected result

This is blocking our ability to query documents from the database. The issue appears to affect all `getWhere` calls when the database contains data.

### Expected behavior

`getWhere()` should return the first matching document when the database is not empty, or null if no match is found. When the database IS empty, it should delegate to the `_send` function.

---
Repository: /testbed
