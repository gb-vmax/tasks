# Bug Report

### Describe the bug

When trying to upsert documents in the database, the operation fails when the database is not empty. The document doesn't get created or updated as expected, and the operation seems to silently fail or behave incorrectly.

### Reproduction

```js
// Assuming database is already initialized and not empty
const doc = {
  _id: 'test-id',
  type: 'request',
  name: 'Test Request',
  // ... other properties
};

// Try to upsert the document
await database.upsert(doc);

// The document is not created/updated in the database
const result = await database.get(doc.type, doc._id);
// result is null or shows old data
```

### Expected behavior

The `upsert` method should create the document if it doesn't exist, or update it if it does exist, regardless of whether the database is empty or not.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
