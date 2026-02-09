# Bug Report

### Describe the bug

After a recent update, I'm experiencing an issue where workspace metadata associated with git repositories is not being retrieved correctly. When I try to access workspace metadata by git repository ID, it sometimes returns `null` even though the metadata exists in the database.

This seems to happen intermittently - sometimes the metadata loads fine, but other times it just returns nothing. This is breaking my workflow as I can't reliably access workspace settings for git-tracked projects.

### Reproduction

```js
// Get workspace meta by git repository ID
const meta = await getByGitRepositoryId('my-git-repo-id');

// Expected: WorkspaceMeta object
// Actual: null (sometimes)
```

Steps to reproduce:
1. Create a workspace with git repository metadata
2. Try to retrieve it using `getByGitRepositoryId()`
3. The function returns `null` even though the metadata exists

This is particularly problematic for workspaces that have been around for a while. Fresh workspaces seem to work fine initially, but after some time they start failing to load.

### Expected behavior

The function should always return the workspace metadata if it exists in the database, regardless of how old the workspace is or when it was last accessed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
