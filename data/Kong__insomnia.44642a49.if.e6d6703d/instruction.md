# Bug Report

### Describe the bug

After a recent update, `getWhere` queries are returning stale data when the underlying documents are modified. The database seems to be caching query results but not properly invalidating the cache when changes occur.

### Reproduction

```js
// Create a document
const workspace = await database.create({
  type: 'Workspace',
  name: 'Test Workspace',
  parentId: null
});

// Query for it
const result1 = await database.getWhere('Workspace', { _id: workspace._id });
console.log(result1.name); // Output: "Test Workspace"

// Update the document
await database.update(workspace, { name: 'Updated Workspace' });

// Query again with the same criteria
const result2 = await database.getWhere('Workspace', { _id: workspace._id });
console.log(result2.name); // Output: "Test Workspace" (WRONG!)
```

### Expected behavior

The second query should return the updated document with `name: 'Updated Workspace'`, not the cached version from before the update.

### Additional context

This is breaking several workflows where we query for documents, modify them, and then query again. The stale cached results are causing the UI to display outdated information until the cache expires (appears to be after 5 seconds).

---
Repository: /testbed
