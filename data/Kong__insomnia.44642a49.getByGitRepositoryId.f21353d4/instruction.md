# Bug Report

### Describe the bug

When trying to retrieve workspace metadata by git repository ID, the function returns an empty array instead of the actual workspace metadata. This appears to happen even when valid git repository IDs are provided.

### Reproduction

```js
// Assuming a workspace exists with gitRepositoryId = 'repo123'
const meta = await getByGitRepositoryId('repo123');

// Expected: WorkspaceMeta object
// Actual: Empty array []
```

### Steps to reproduce
1. Create a workspace with an associated git repository
2. Try to fetch the workspace metadata using `getByGitRepositoryId()` with the repository ID
3. The function returns an empty array instead of the workspace metadata

### Expected behavior
The function should return the workspace metadata object when a valid git repository ID is provided, not an empty array.

### Additional context
This seems to have started happening recently. The function is returning empty arrays for repository IDs that definitely exist in the database.

---
Repository: /testbed
