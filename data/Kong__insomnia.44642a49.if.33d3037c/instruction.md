# Bug Report

### Describe the bug

I'm experiencing an issue where calling `database.remove()` on a document doesn't actually remove it from the database. Instead, it seems to be clearing the entire database or doing something unexpected. The document I'm trying to delete remains in the database, but other unrelated documents might be affected.

### Reproduction

```js
// Create and save a document
const doc = await database.insert({
  type: 'Request',
  name: 'My Request',
  // ... other properties
});

// Try to remove the specific document
await database.remove(doc);

// Expected: doc should be removed
// Actual: doc is still there, or wrong operation is performed
```

### Expected behavior

When calling `database.remove(doc)`, only the specified document should be removed from the database. Other documents should remain untouched.

### System Info

- Insomnia version: latest
- OS: macOS

This seems to have started recently. Not sure if it's related to any recent changes in the database module but it's breaking document deletion functionality.

---
Repository: /testbed
