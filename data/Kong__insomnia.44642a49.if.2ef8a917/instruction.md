# Bug Report

### Describe the bug

When trying to delete certain environment or cookie jar documents, the application throws an error saying "Cannot remove critical document" even though the document should be safe to delete. This appears to be blocking normal deletion workflows.

### Reproduction

```js
// Create a workspace with multiple environments
const workspace = await database.get(models.workspace.type, workspaceId);

// Create two environments under the workspace
const env1 = await models.environment.create({
  parentId: workspace._id,
  name: 'Environment 1'
});

const env2 = await models.environment.create({
  parentId: workspace._id,
  name: 'Environment 2'
});

// Try to delete env1 - this should work but throws an error
await database.unsafeRemove(env1);
// Error: Cannot remove critical document: environment <id>
```

The same issue happens with cookie jars when there are multiple cookie jars in a workspace.

### Expected behavior

The document should be deleted successfully when there are multiple environments/cookie jars in the workspace. The protection should only apply when trying to delete the last remaining environment or cookie jar.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
