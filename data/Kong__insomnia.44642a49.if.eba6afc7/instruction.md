# Bug Report

### Describe the bug

The `database.withAncestors()` function is returning an empty array when the database is not empty, which is the opposite of the expected behavior. This causes ancestor lookup to fail in normal operation.

### Reproduction

```js
// Assuming database is initialized and not empty
const doc = await database.get('SomeModel', 'some-id');
const ancestors = await database.withAncestors(doc, ['workspace', 'project']);

// Expected: Array of ancestor documents
// Actual: Empty array []
```

### Expected behavior

When the database is populated (not empty), `withAncestors()` should return the ancestor chain for the given document. It should only return an empty array when the document itself is null/undefined, not when the database has data.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
