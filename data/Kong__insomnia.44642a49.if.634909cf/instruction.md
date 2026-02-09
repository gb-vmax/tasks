# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with document updates in the database. When I try to update a document, the operation seems to hang indefinitely and never completes. The application becomes unresponsive when performing update operations.

### Reproduction

```js
const doc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  modified: Date.now()
};

// This operation never completes
await database.update(doc);
console.log('This line is never reached');
```

### Expected behavior

The `database.update()` function should complete successfully and update the document in the database. The promise should resolve with the updated document.

### Additional context

This seems to have started happening after the latest changes. The update function appears to be stuck and doesn't return. I've tried with different document types (Request, Environment, etc.) and they all exhibit the same behavior.

The issue occurs consistently on every update attempt, making it impossible to modify any documents in the application.

---
Repository: /testbed
