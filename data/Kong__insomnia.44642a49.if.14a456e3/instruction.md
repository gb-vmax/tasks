# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with stale data being returned when querying for the most recently modified documents in the database. It seems like the system is caching results and not properly invalidating them when documents are updated.

### Reproduction

```js
// Create or update a document
await database.update(doc, { name: 'Updated Name' });

// Immediately query for most recently modified
const result = await database.getMostRecentlyModified('Request', { parentId: workspaceId });

// Expected: Returns the updated document
// Actual: Sometimes returns an older version of the document or stale data
```

The issue appears to be intermittent but becomes more noticeable when:
1. Rapidly updating documents
2. Querying with different query parameters
3. Working with multiple document types

### Expected behavior

`getMostRecentlyModified` should always return the current state of the most recently modified document, not a cached version. When a document is updated, subsequent queries should reflect those changes immediately.

### Additional context

This is causing issues in our workflow where we update a request and then immediately try to fetch it to display in the UI. The UI shows outdated information until we manually refresh or wait a few seconds.

System: Insomnia latest version

---
Repository: /testbed
