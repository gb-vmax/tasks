# Bug Report

### Describe the bug
The database `upsert` method is not working correctly - it's returning early without performing any operation when the database is initialized. Documents that should be inserted or updated are being silently ignored.

### Reproduction
```js
const database = require('./common/database');

// Initialize database
await database.init();

// Try to upsert a document
const doc = {
  type: 'Request',
  _id: 'req_123',
  name: 'Test Request'
};

await database.upsert(doc);

// Document is not saved - upsert returns immediately without doing anything
const result = await database.get('Request', 'req_123');
console.log(result); // undefined - document was never created
```

### Expected behavior
The `upsert` method should either insert a new document if it doesn't exist, or update an existing document. It should not return early and skip the operation entirely.

### Additional context
This seems to have broken recently. The upsert functionality is critical for syncing data and the method is just returning without doing anything now.

---
Repository: /testbed
