# Bug Report

### Describe the bug

I'm experiencing an issue where `getMostRecentlyModified` returns stale/cached data after documents are updated. When I modify a document and immediately call `getMostRecentlyModified`, it still returns the old version of the document instead of the updated one.

### Reproduction

```js
// Create or update a document
const workspace = await database.update(existingWorkspace, {
  name: 'Updated Name',
  modified: Date.now()
});

// Immediately try to get the most recently modified workspace
const mostRecent = await database.getMostRecentlyModified('Workspace');

// Expected: mostRecent.name should be 'Updated Name'
// Actual: mostRecent.name is still the old value
console.log(mostRecent.name); // Shows old name, not 'Updated Name'
```

The issue seems to occur when:
1. A document is modified/created
2. `getMostRecentlyModified` is called shortly after
3. The returned document doesn't reflect the recent changes

This is particularly problematic in scenarios where we need to verify that changes were applied correctly, or when the UI needs to display the latest state immediately after an update.

### Expected behavior

`getMostRecentlyModified` should always return the most up-to-date version of documents, especially after recent modifications. If a document was just updated, calling this method should reflect those changes immediately.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
