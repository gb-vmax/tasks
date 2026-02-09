# Bug Report

### Describe the bug

After a recent update, I'm getting version conflict errors when trying to update documents in the database. The error message says something like "Version conflict: Document X has been modified. Expected version Y, but current version is Z".

This is happening even when I'm just doing a simple update to a document that I just retrieved. The document hasn't been modified by anything else, but the update is still being rejected.

### Reproduction

```js
// Get a document from the database
const doc = await database.get('request', 'req_123');

// Try to update it
doc.name = 'Updated Name';
await database.update(doc);

// Error: Version conflict: Document req_123 has been modified...
```

This also happens when creating a new document and then immediately trying to update it:

```js
const newDoc = await database.insert({
  type: 'request',
  name: 'Test Request',
  // ... other fields
});

// Modify something
newDoc.name = 'Modified Name';

// This fails with version conflict
await database.update(newDoc);
```

### Expected behavior

The update should succeed without any version conflict errors. If I just retrieved the document or created it, there shouldn't be any version mismatch when I try to update it.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow as I can't update any documents anymore. Any help would be appreciated!

---
Repository: /testbed
