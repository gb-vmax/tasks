# Bug Report

### Describe the bug

The duplicate function is failing when trying to copy documents in the database. The operation appears to be incomplete and causes the application to break when attempting to duplicate any item (requests, folders, etc.).

### Reproduction

```js
// Try to duplicate any document with a name
const originalDoc = {
  _id: 'req_123',
  type: 'Request',
  name: 'My Request',
  parentId: 'wrk_abc',
  // ... other properties
};

await database.duplicate(originalDoc);
// Application crashes or hangs
```

### Expected behavior

The duplicate operation should complete successfully and create a copy of the document with a unique name (e.g., "My Request (Copy)"). The duplicated item should appear in the UI alongside the original.

### Additional context

This seems to have broken recently. When I try to duplicate a request or folder, nothing happens or the app becomes unresponsive. The duplication feature was working fine before.

---
Repository: /testbed
