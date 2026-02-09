# Bug Report

### Describe the bug

I'm experiencing a critical issue with the database update functionality. When attempting to update documents in the database, the documents are being deleted instead of updated. This is causing data loss in my application.

### Reproduction

```js
// Create a document
const doc = await database.insert({
  type: 'request',
  name: 'My Request',
  url: 'https://example.com'
});

// Try to update the document
const updatedDoc = await database.update({
  ...doc,
  name: 'Updated Request Name'
});

// Expected: Document is updated with new name
// Actual: Document is deleted from the database
```

### Expected behavior

When calling `database.update()` with a document, it should update the existing document in the database with the new values. The document should remain in the database with its updated properties.

### Actual behavior

Instead of updating the document, it gets deleted from the database entirely. This is causing significant data loss issues.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like a regression as updates were working fine before. Any help would be greatly appreciated!

---
Repository: /testbed
