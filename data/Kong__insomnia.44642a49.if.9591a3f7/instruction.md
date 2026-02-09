# Bug Report

### Describe the bug

After a recent update, the database insert operation seems to be broken. When trying to insert documents into the database, the operation hangs indefinitely and never completes. The application becomes unresponsive when attempting to create new resources.

### Reproduction

```js
const newDocument = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  // ... other properties
};

// This call never resolves
await database.insert(newDocument);
console.log('This line is never reached');
```

### Expected behavior

The insert operation should complete successfully and return the newly inserted document. The application should remain responsive and continue normal operation.

### Additional context

This appears to affect all document types (Request, RequestGroup, Workspace, etc.). The issue started appearing after updating to the latest version. Rolling back to the previous version resolves the problem.

The hang occurs even with simple documents and doesn't seem to be related to document size or complexity. No error messages are logged to the console.

---
Repository: /testbed
