# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with `getMostRecentlyModified` returning stale data. When I modify a document and immediately query for the most recently modified document of that type, it sometimes returns the old version instead of the updated one.

### Reproduction

```js
// Create a document
const doc = await database.insert({
  type: 'request',
  name: 'Test Request',
  modified: Date.now()
});

// Get most recent - works fine
const recent1 = await database.getMostRecentlyModified('request');
console.log(recent1.name); // "Test Request"

// Update the document
await database.update({
  ...doc,
  name: 'Updated Request',
  modified: Date.now()
});

// Get most recent again - returns old data
const recent2 = await database.getMostRecentlyModified('request');
console.log(recent2.name); // Still shows "Test Request" instead of "Updated Request"
```

### Expected behavior

`getMostRecentlyModified` should always return the most up-to-date version of the document after modifications. The function should reflect changes immediately after `update`, `insert`, or `remove` operations.

### Additional context

This seems to happen inconsistently - sometimes it works correctly, other times it returns stale data. It's particularly noticeable when making rapid updates to documents and then querying for the most recent one.

---
Repository: /testbed
