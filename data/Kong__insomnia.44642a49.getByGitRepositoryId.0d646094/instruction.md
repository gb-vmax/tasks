# Bug Report

### Describe the bug

I'm experiencing an issue with Git repository integration where workspace metadata cannot be retrieved correctly. When trying to fetch workspace metadata by Git repository ID, the lookup is failing and returning null even though the workspace exists and has a valid Git repository associated with it.

### Reproduction

```js
// Create a workspace with Git repository
const workspace = await createWorkspace({
  name: 'My Project',
  gitRepositoryId: 'repo-123'
});

// Try to fetch the workspace meta by Git repository ID
const workspaceMeta = await getByGitRepositoryId('repo-123');

// Returns null instead of the workspace metadata
console.log(workspaceMeta); // null
```

### Expected behavior

The function should return the workspace metadata object when a valid Git repository ID is provided. The workspace metadata should be retrievable using the same ID that was used when creating/linking the Git repository.

### Additional context

This seems to have started happening recently. The workspace metadata exists in the database but the query isn't finding it. Other lookup methods (like `getByParentId`) work fine, so it's specific to the Git repository ID lookup.

---
Repository: /testbed
