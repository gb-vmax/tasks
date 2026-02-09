# Bug Report

### Describe the bug

After a recent update, the `removeWhere` function is broken and causing syntax errors. When trying to remove documents from the database using `removeWhere`, the application crashes immediately.

### Reproduction

```js
// Try to remove documents matching a query
await database.removeWhere('Request', { parentId: workspaceId });
```

The code fails to execute and throws a syntax error. This is blocking our ability to delete any documents from the database.

### Expected behavior

The `removeWhere` function should successfully remove all documents matching the given query without any syntax errors, just like it did in previous versions.

### Additional context

This appears to have broken recently - the function was working fine before. The database operations are completely broken now and we can't perform any deletions.

---
Repository: /testbed
