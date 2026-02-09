# Bug Report

### Describe the bug

When trying to retrieve workspace metadata by git repository ID, the function `getByGitRepositoryId` is not returning the expected results. It appears to be querying with the wrong field name, causing lookups to fail.

### Reproduction

```js
// Assuming you have a workspace with git repository metadata
const gitRepoId = 'repo_123456';

// Try to get workspace meta by git repository ID
const workspaceMeta = await getByGitRepositoryId(gitRepoId);

// Returns null/undefined even though the workspace exists
console.log(workspaceMeta); // Expected: WorkspaceMeta object, Actual: null
```

### Expected behavior

The function should correctly query the database using the `gitRepositoryId` field and return the corresponding `WorkspaceMeta` object when it exists.

### Additional context

This seems to affect any workflow that relies on looking up workspace metadata by git repository ID. The database query appears to be using an incorrect field name for the lookup.

---
Repository: /testbed
