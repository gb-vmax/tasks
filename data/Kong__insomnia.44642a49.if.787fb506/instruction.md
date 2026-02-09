# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with database document retrieval. When I fetch a document, modify it, and then fetch it again within a short time window, the changes aren't reflected - I'm getting the old version of the document instead of the updated one.

### Reproduction

```js
// Fetch a document
const workspace = await database.get('Workspace', 'wrk_123');
console.log(workspace.name); // Output: "My Workspace"

// Update the document
await database.update(workspace, { name: "Updated Workspace" });

// Fetch the same document again immediately
const refreshedWorkspace = await database.get('Workspace', 'wrk_123');
console.log(refreshedWorkspace.name); // Output: "My Workspace" (expected: "Updated Workspace")
```

The second fetch returns stale data even though the document was just updated. This only seems to happen when fetching the same document multiple times in quick succession (within a few seconds).

### Expected behavior

`database.get()` should always return the most recent version of a document from the database, especially after an update operation.

### Additional context

This is causing issues in our workflows where we need to refresh document state after modifications. The problem seems to appear randomly but is more consistent when operations happen quickly one after another.

---
Repository: /testbed
