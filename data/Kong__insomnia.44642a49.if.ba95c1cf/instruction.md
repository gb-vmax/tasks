# Bug Report

### Describe the bug

I'm experiencing an issue where documents cannot be removed from the database when they are referenced by other documents. The removal operation throws an error about external references even though the referenced document should be allowed to be deleted.

### Reproduction

```js
// Create a workspace and a request that references it
const workspace = await database.insert({
  type: 'Workspace',
  name: 'My Workspace',
  // ... other fields
});

const request = await database.insert({
  type: 'Request',
  name: 'My Request',
  parentId: workspace._id,
  // ... other fields with workspace._id in some property
});

// Try to remove the workspace
await database.remove(workspace);
// Error: Cannot remove Workspace <id>: referenced by 1 other document(s)
```

### Expected behavior

The document should be removed successfully. If the model supports soft deletion, it should be soft-deleted. Otherwise, it should be removed along with its descendants without checking for external references in cases where the reference is part of the normal parent-child relationship or expected usage pattern.

The current behavior is blocking legitimate deletion operations because it's detecting references that shouldn't prevent deletion.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
