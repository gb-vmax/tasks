# Bug Report

### Describe the bug

After a recent update, I'm seeing stale data being returned from `database.get()` calls. When I update a document and then immediately fetch it again, the old version is returned instead of the updated one.

### Reproduction

```js
// Get initial document
const doc = await database.get('request', 'req_123');
console.log(doc.name); // "Original Name"

// Update the document
await database.update(doc, { name: "Updated Name" });

// Get the document again
const updatedDoc = await database.get('request', 'req_123');
console.log(updatedDoc.name); // Still shows "Original Name" instead of "Updated Name"
```

The same issue happens when:
1. Updating a document through one part of the application
2. Fetching it from another part
3. Getting the old cached version instead of the fresh data

This is causing data consistency issues throughout the app where different components show different versions of the same document.

### Expected behavior

`database.get()` should always return the most current version of a document, especially after it has been modified.

### Additional context

This seems to have started happening recently. I suspect it might be related to some caching mechanism, but the cached data isn't being properly invalidated when documents change.

---
Repository: /testbed
