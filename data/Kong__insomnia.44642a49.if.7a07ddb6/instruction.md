# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with document updates in the database. When trying to update documents, the operation seems to fail silently or hang indefinitely without completing. The application becomes unresponsive when attempting to save changes to any document.

### Reproduction

```js
const doc = await database.get('request', 'req_123');
doc.name = 'Updated Request Name';

// This call never resolves
await database.update(doc);
```

The update operation doesn't complete and the promise never resolves. This is blocking all save operations in the application.

### Expected behavior

The `database.update()` method should successfully update the document and resolve the promise with the updated document object.

### System Info
- Insomnia version: latest
- OS: macOS

This is a critical issue as it prevents saving any changes to documents. Any help would be appreciated!

---
Repository: /testbed
