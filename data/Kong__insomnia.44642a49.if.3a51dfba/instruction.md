# Bug Report

### Describe the bug

I'm experiencing an issue where database upsert operations seem to hang indefinitely and never complete. The application becomes unresponsive when trying to update or insert documents.

### Reproduction

```js
const doc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  modified: Date.now()
};

// This call never completes
await database.upsert(doc);
console.log('This line is never reached');
```

### Expected behavior

The `upsert` operation should complete successfully and return the updated/inserted document. The code after the upsert call should execute normally.

### Additional context

This started happening recently and affects all document types. The application freezes when performing any upsert operation, making it impossible to save changes. I have to force quit the application.

It seems like the operation gets stuck somewhere in the middle of processing. No error is thrown, it just hangs forever.

---
Repository: /testbed
