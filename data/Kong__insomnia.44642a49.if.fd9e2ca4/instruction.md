# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where document insertions into the database are failing. When I try to insert a new document, nothing happens and the operation seems to hang indefinitely. The application becomes unresponsive when attempting to create new requests, workspaces, or any other database entities.

### Reproduction

```js
const newRequest = {
  _id: 'req_123',
  type: 'Request',
  parentId: 'wrk_456',
  name: 'My Request',
  url: 'https://api.example.com',
  method: 'GET',
  created: Date.now(),
  modified: Date.now()
};

// This operation never completes
await database.insert(newRequest);
```

### Expected behavior

The document should be inserted into the database successfully and the operation should complete normally. The UI should update to reflect the newly created item.

### Additional context

This seems to affect all document types - requests, folders, environments, etc. The issue started appearing after updating to the latest version. Rolling back to the previous version resolves the problem.

The database appears to be working fine for other operations like `find()` and `update()`, only `insert()` seems to be affected.

---
Repository: /testbed
