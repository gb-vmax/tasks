# Bug Report

### Describe the bug

When calling `withDescendants()` on a document, the function returns an empty array instead of the document and its descendants. This appears to happen when the database is not empty.

### Reproduction

```js
const doc = await database.getById('some-id');
const descendants = await database.withDescendants(doc);

// Expected: [doc, ...child documents]
// Actual: []
```

### Steps to reproduce
1. Initialize a database with some documents
2. Retrieve a document that has child documents
3. Call `withDescendants()` on that document
4. The function returns an empty array instead of the document tree

### Expected behavior

The function should return an array containing the document itself and all its descendants, stopping at the specified `stopType` if provided.

### Additional context

This seems to affect the document tree traversal functionality. The method is supposed to recursively collect all descendant documents but instead returns nothing when the database has data.

---
Repository: /testbed
