# Bug Report

### Describe the bug

The `withAncestors` function is returning an empty array instead of fetching ancestor documents when the database is not empty. This causes issues when trying to retrieve parent/ancestor relationships for documents.

### Reproduction

```js
// Assuming database is initialized and not empty
const doc = await database.get('some-document-id');
const ancestors = await database.withAncestors(doc, ['workspace', 'folder']);

// Expected: Array of ancestor documents
// Actual: Empty array []
```

### Expected behavior

When calling `withAncestors` on a document with an initialized database, it should return an array containing all ancestor documents matching the specified types. Currently it's returning an empty array even when ancestors exist.

### Additional context

This appears to affect any code that relies on traversing the document hierarchy. The function seems to be taking the wrong code path based on the database state check.

---
Repository: /testbed
