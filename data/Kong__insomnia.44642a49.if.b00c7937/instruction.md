# Bug Report

### Describe the bug

When trying to insert documents into the database, the insert operation appears to fail silently when the database is not empty. Documents are not being persisted and no error is thrown, making it difficult to debug.

### Reproduction

```js
// Initialize database with some data
await database.insert(someDocument);

// Try to insert another document
const newDoc = {
  _id: 'doc_123',
  type: 'request',
  name: 'Test Request'
};

const result = await database.insert(newDoc);
// result is undefined, document is not inserted
```

### Expected behavior

The `insert` function should successfully insert documents into the database regardless of whether the database is empty or not, and return the inserted document.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
