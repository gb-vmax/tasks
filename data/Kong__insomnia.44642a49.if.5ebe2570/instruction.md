# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database insertions. When trying to insert documents, the operation seems to hang or fail silently without any clear error message. This is breaking my workflow where I need to insert multiple documents programmatically.

### Reproduction

```js
const newRequest = {
  _id: 'req_123',
  type: 'Request',
  parentId: 'wrk_456',
  name: 'My Request',
  // ... other fields
};

// This operation doesn't complete as expected
await database.insert(newRequest);
```

The insert operation doesn't seem to return properly. I've also noticed that when I try to insert documents with the same name in the same workspace, the behavior is inconsistent - sometimes it seems to work, other times it doesn't.

### Expected behavior

The `insert()` function should:
1. Complete successfully when inserting valid documents
2. Return the inserted document
3. Handle duplicate names/fields consistently (either allow them or reject with a clear error)

### System Info
- Insomnia version: Latest
- OS: macOS

This is blocking my ability to programmatically create requests and environments. Any help would be appreciated!

---
Repository: /testbed
