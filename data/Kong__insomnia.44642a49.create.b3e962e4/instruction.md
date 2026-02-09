# Bug Report

### Describe the bug
I'm encountering an issue when trying to create a new WorkspaceMeta object. The function seems to be failing silently or not creating the workspace metadata correctly.

### Reproduction
```js
const workspaceMeta = await create({
  parentId: 'workspace_123',
  // other properties...
});
```

When I call the `create()` function with a valid `parentId`, the workspace metadata doesn't get created as expected. It seems like the arguments might be in the wrong order or something similar is happening internally.

### Expected behavior
The `create()` function should properly create a WorkspaceMeta document in the database with the provided patch data and associate it with the correct type.

### Additional context
This might be related to how the `db.docCreate` method is being called. The workspace metadata creation was working fine in previous versions but seems to have broken recently.

---
Repository: /testbed
