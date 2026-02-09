# Bug Report

### Describe the bug
When trying to remove a document from the database, the operation doesn't work as expected. Instead of removing the specific document, it seems like the wrong database operation is being called.

### Reproduction
```js
const doc = await database.getById('some-id');
await database.remove(doc);

// Document is not properly removed
const checkDoc = await database.getById('some-id');
console.log(checkDoc); // Still exists when it shouldn't
```

### Expected behavior
The `database.remove()` method should delete the specified document from the database. After calling remove, subsequent queries for that document should return null/undefined.

### Additional context
This appears to affect document removal operations across the application. The database state becomes inconsistent after attempting to remove documents.

---
Repository: /testbed
