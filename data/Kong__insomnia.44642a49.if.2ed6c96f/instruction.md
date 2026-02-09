# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database document retrieval where stale data is being returned even after documents have been updated. The system seems to be caching documents but not properly invalidating the cache when changes occur.

### Reproduction

```js
// Create a document
const doc = await database.insert({ type: 'request', name: 'Test Request' });

// Update the document
await database.update({ ...doc, name: 'Updated Request' });

// Retrieve the document again
const retrieved = await database.get('request', doc._id);

// Retrieved document still has the old name 'Test Request' instead of 'Updated Request'
console.log(retrieved.name); // Expected: 'Updated Request', Actual: 'Test Request'
```

### Expected behavior

When a document is updated and then retrieved using `database.get()`, it should return the latest version of the document, not a cached stale version.

### Additional context

This appears to happen consistently when:
1. A document is first retrieved (gets cached)
2. The document is then updated through `database.update()`
3. The same document is retrieved again using `database.get()`

The cached version from step 1 is returned instead of the updated version from step 2.

---
Repository: /testbed
