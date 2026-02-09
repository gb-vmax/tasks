# Bug Report

### Describe the bug

After a recent update, I'm seeing stale data being returned from `getMostRecentlyModified()`. When I modify a document and immediately query for the most recently modified document of that type, I'm getting back an older version instead of the updated one.

### Reproduction

```js
// Create or update a document
const workspace = await database.update(existingWorkspace, {
  name: 'Updated Workspace Name',
  modified: Date.now()
});

// Immediately query for most recently modified workspace
const mostRecent = await database.getMostRecentlyModified('Workspace');

// Expected: mostRecent should be the updated workspace
// Actual: Getting back an older version with the old name
console.log(mostRecent.name); // Shows old name instead of 'Updated Workspace Name'
```

This seems to happen consistently when:
1. Updating an existing document
2. Immediately calling `getMostRecentlyModified()` for that document type
3. The returned document doesn't reflect the recent changes

### Expected behavior

`getMostRecentlyModified()` should always return the actual most recently modified document, not a cached or stale version. After updating a document, the next call to `getMostRecentlyModified()` should reflect those changes.

### Additional context

This started happening after the latest changes. It's affecting our workflow where we need to immediately access updated documents. Sometimes refreshing or waiting a bit seems to help, but it's inconsistent.

---
Repository: /testbed
