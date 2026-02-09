# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database document retrieval. When I fetch a document, update it, and then fetch it again, I'm getting stale/cached data instead of the updated version. The changes are persisted to the database but subsequent `get` calls return the old data.

### Reproduction

```js
// Fetch a document
const doc = await database.get('Request', 'req_123');
console.log(doc.name); // Output: "Original Name"

// Update the document
await database.update(doc, { name: "Updated Name" });

// Fetch the same document again
const updatedDoc = await database.get('Request', 'req_123');
console.log(updatedDoc.name); // Expected: "Updated Name", Actual: "Original Name"
```

The issue seems to be that the `get` method is returning cached data that doesn't reflect recent changes. This is causing the UI to display outdated information even after successful updates.

### Expected behavior

The `database.get()` method should always return the most recent version of a document from the database, especially after updates have been made.

### System Info
- Version: Latest
- OS: macOS

This is blocking our workflow as users are seeing stale data after making changes. Any help would be appreciated!

---
Repository: /testbed
