# Bug Report

### Describe the bug

When working with the Git VCS integration, I'm encountering issues where certain git operations fail unexpectedly. It seems like some methods are being called before the repository is properly initialized, but there's no clear error message or indication of what went wrong.

### Reproduction

```js
const gitVCS = new GitVCS();

// Try to list files without initializing first
await gitVCS.listFiles();

// Or try to get current branch
await gitVCS.getCurrentBranch();
```

The operations just fail silently or throw unclear errors, making it difficult to debug what's happening.

### Expected behavior

When git operations are called on an uninitialized repository, there should be a clear error message indicating that the repository needs to be initialized first via `init()` or `initFromClone()`.

### Additional context

This makes it really hard to track down issues when the git integration isn't working. It would be helpful if there was some validation to ensure the repo is initialized before attempting operations like listing files, branches, or fetching remote branches.

---
Repository: /testbed
