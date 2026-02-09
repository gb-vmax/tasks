# Bug Report

### Describe the bug

After a recent update, the `unsafeRemove` function in the database module is not working correctly. When trying to remove documents, the operation fails and nothing gets deleted from the database.

### Reproduction

```js
const workspace = await database.create({
  type: 'workspace',
  name: 'Test Workspace',
  parentId: null
});

// This should remove the workspace but doesn't work
await database.unsafeRemove(workspace);

// The workspace is still in the database
const found = await database.getById('workspace', workspace._id);
console.log(found); // Still returns the workspace object
```

### Expected behavior

The `unsafeRemove` function should delete the document from the database. The document should no longer be retrievable after the removal operation completes.

### Additional context

This appears to have broken recently. The function seems to be doing some logging about orphaned children but then doesn't actually perform the removal. I noticed this when trying to clean up test data in my workflow.

---
Repository: /testbed
