# Bug Report

### Describe the bug

The `upsert` method is not working correctly when the database is empty. It seems like the logic for handling empty database state got inverted somehow. When I try to upsert documents into an empty database, nothing happens - the documents aren't being saved.

### Reproduction

```js
// Start with empty database
const db = database;

// Try to upsert a new document
const doc = {
  _id: 'req_123',
  type: 'Request',
  name: 'Test Request',
  // ... other properties
};

await database.upsert(doc);

// Document is not saved - database remains empty
const result = await database.get('Request', 'req_123');
console.log(result); // undefined - document wasn't saved
```

### Expected behavior

The `upsert` method should save the document to the database regardless of whether the database is empty or not. When upserting to an empty database, it should create the document. When upserting to a non-empty database, it should either update an existing document or create a new one.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my workflow since I can't create new workspaces or requests in fresh installations.

---
Repository: /testbed
