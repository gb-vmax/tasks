# Bug Report

### Describe the bug

The database `upsert` method is not working correctly - it seems to be checking the wrong condition for when to send the operation. When the database is not empty, the upsert operation completes immediately without actually checking if the document exists or performing the insert/update logic.

### Reproduction

```js
// Assuming database is initialized and not empty
const doc = {
  type: 'request',
  _id: 'req_123',
  name: 'Test Request',
  // ... other properties
};

// Try to upsert a document
await database.upsert(doc);

// The method returns early without checking if doc exists
// or performing the actual upsert operation
```

### Expected behavior

The `upsert` method should:
1. Check if the document exists in the database
2. If it exists, update it
3. If it doesn't exist, insert it as a new document

This should work regardless of whether the database is empty or not.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
