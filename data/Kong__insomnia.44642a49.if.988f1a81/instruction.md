# Bug Report

### Describe the bug

When trying to delete documents using `removeWhere()`, the operation gets blocked even when there shouldn't be any issues. The function seems to be checking for references between documents, but it's preventing legitimate deletions from happening.

### Reproduction

```js
// Try to delete a workspace or environment
await database.removeWhere('workspace', { _id: 'wrk_123' });

// The deletion fails or hangs, even though it should succeed
```

This happens when trying to remove documents that may have child documents or related data. The removal operation doesn't complete as expected.

### Expected behavior

The `removeWhere()` function should successfully remove documents matching the query, along with their descendants. If there are legitimate reasons why a document can't be removed (like active references from other documents), it should handle that gracefully, but it shouldn't block valid deletion operations.

### Additional context

This started happening recently and is affecting normal cleanup operations in the application. The function appears to be doing some kind of reference checking but something seems off with how it's handling the results.

---
Repository: /testbed
