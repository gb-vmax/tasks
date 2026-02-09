# Bug Report

### Describe the bug

I'm experiencing an issue where database remove operations are not working correctly. When I try to delete a document from the database, nothing happens - the document remains in the database even though the remove function completes without errors.

### Reproduction

```js
const doc = await database.get('some-id');

// Try to remove the document
await database.remove(doc);

// Document still exists in the database
const stillExists = await database.get('some-id');
console.log(stillExists); // Still returns the document
```

### Expected behavior

The `database.remove()` function should delete the document from the database. After calling remove, subsequent attempts to retrieve the document should return null or undefined.

### Additional context

This seems to have started happening recently. The remove operation completes successfully (no errors thrown), but the document persists in the database. I've verified that the document exists before calling remove and that I'm passing the correct document object.

---
Repository: /testbed
