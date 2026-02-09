# Bug Report

### Describe the bug

The `getByGitRepositoryId` function in workspace-meta is not returning workspace metadata correctly. When trying to retrieve workspace metadata by git repository ID, the function appears to be passing the wrong arguments to the database query.

### Reproduction

```js
const workspaceMeta = await getByGitRepositoryId('my-repo-id');
// Returns unexpected results or fails to find the workspace metadata
```

### Expected behavior

The function should return the workspace metadata associated with the given git repository ID by properly querying the database with the correct field filter.

### Additional context

This is affecting git repository synchronization features where workspace metadata needs to be looked up by repository ID. The function signature suggests it should accept a `gitRepositoryId` string parameter and return matching workspace metadata, but the current implementation doesn't seem to be querying correctly.

---
Repository: /testbed
