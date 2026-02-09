# Bug Report

### Describe the bug

The `database.get()` function is not retrieving data correctly. When attempting to fetch database records by ID, the function returns undefined or fails to return the expected data even when the database is populated and the ID exists.

### Reproduction

```js
// Initialize database with some data
await database.insert({
  type: 'workspace',
  _id: 'wrk_123',
  name: 'My Workspace'
});

// Try to retrieve the data
const workspace = await database.get('workspace', 'wrk_123');

// workspace is undefined or not what was inserted
console.log(workspace); // Expected: { type: 'workspace', _id: 'wrk_123', name: 'My Workspace' }
```

### Expected behavior

The `database.get()` method should return the correct record when provided with a valid type and ID. The retrieved object should match what was previously inserted into the database.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The database insert operations work fine, but retrieval is broken.

---
Repository: /testbed
