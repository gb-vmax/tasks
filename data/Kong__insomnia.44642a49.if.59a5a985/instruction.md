# Bug Report

### Describe the bug
When trying to retrieve the most recently modified document using `getMostRecentlyModified()`, the function returns `null` even when documents exist in the database. This appears to be a regression as it was working correctly before.

### Reproduction
```js
// Assume we have some documents in the database
await database.insert({
  type: 'Request',
  name: 'Test Request',
  modified: Date.now()
});

// Try to get the most recently modified document
const doc = await database.getMostRecentlyModified('Request');

// Expected: Should return the document we just inserted
// Actual: Returns null
console.log(doc); // null
```

### Expected behavior
The function should return the most recently modified document of the specified type when documents exist in the database. It should only return `null` when no matching documents are found.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we rely on this function to restore the last active request when reopening the app. Any help would be appreciated!

---
Repository: /testbed
