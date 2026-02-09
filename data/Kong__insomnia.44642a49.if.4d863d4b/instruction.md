# Bug Report

### Describe the bug
I'm experiencing an issue where calling `database.remove()` on a document doesn't actually delete it from the database. The function seems to return without performing any action, and the document remains in the database after the call.

### Reproduction
```js
const doc = await database.getById('some-id');

// Try to remove the document
await database.remove(doc);

// Document still exists in the database
const stillExists = await database.getById('some-id');
console.log(stillExists); // Document is still there
```

### Expected behavior
The document should be removed from the database when `database.remove()` is called. After removal, attempting to retrieve the document by ID should return null or undefined.

### Additional context
This seems to happen consistently across different document types. The function completes without throwing any errors, but the document persists in the database.

---
Repository: /testbed
