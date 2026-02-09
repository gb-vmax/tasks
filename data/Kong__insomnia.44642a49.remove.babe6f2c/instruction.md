# Bug Report

### Describe the bug

After a recent update, removing a Git repository from the workspace is no longer working. The removal operation appears to hang indefinitely and never completes. The repository remains in the workspace even after attempting to delete it.

### Reproduction

```js
const repo = {
  _id: 'repo_123',
  name: 'my-repo',
  uri: 'https://github.com/user/repo.git',
  needsFullClone: false,
  credentials: {
    token: 'github_pat_xxx'
  }
};

// Try to remove the repository
await remove(repo);
// Operation never completes, repository is not removed
```

### Expected behavior

The repository should be removed from the workspace immediately when calling the `remove()` function. The operation should complete successfully and the repository should no longer appear in the workspace.

### System Info

- Insomnia version: Latest
- OS: macOS

---
Repository: /testbed
