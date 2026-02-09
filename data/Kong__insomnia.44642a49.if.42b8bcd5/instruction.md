# Bug Report

### Describe the bug

After a recent update, the `unsafeRemove` function in the database module appears to be broken. When attempting to remove a document, the operation fails and the document is not actually removed from the database.

### Reproduction

```js
const doc = {
  _id: 'test_123',
  type: 'request',
  name: 'Test Request'
};

// Try to remove the document
await database.unsafeRemove(doc);

// Document is still in the database
const result = await database.getWhere('request', { _id: 'test_123' });
console.log(result); // Still returns the document
```

### Expected behavior

The document should be removed from the database when calling `unsafeRemove()`. The function should complete successfully without errors.

### Additional context

This seems to have started happening recently. The `unsafeRemove` function used to work fine for removing entries without removing their children. Now it seems like the removal logic isn't executing properly.

---
Repository: /testbed
