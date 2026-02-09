# Bug Report

### Describe the bug

After a recent update, the database update function appears to be incomplete or corrupted. When trying to update documents in the database, the application hangs or behaves unexpectedly. Looking at the code, it seems like the `update` function definition got malformed during a merge or refactoring.

### Reproduction

```js
const doc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  modified: Date.now()
};

// Try to update the document
await database.update(doc);
// Application hangs or throws unexpected errors
```

### Expected behavior

The `update` function should complete successfully and return the updated document. The function should be properly defined and callable without hanging or causing runtime errors.

### Additional context

This seems to have broken basic document update operations. The function signature looks incomplete in the source code - it appears to start a Promise but doesn't have proper completion or closing braces. This is blocking any workflow that needs to update documents in the database.

### System Info
- Insomnia packages version: latest
- Node version: 18.x

---
Repository: /testbed
