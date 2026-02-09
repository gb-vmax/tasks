# Bug Report

### Describe the bug

After a recent update, the Git integration seems to be caching branch information even after operations that should change it. When I initialize a new repository or clone an existing one, subsequent calls to get the current branch return stale cached data instead of the actual current branch.

### Reproduction

```js
const gitVCS = new GitVCS();

// Initialize a new repo
await gitVCS.init({
  directory: '/path/to/repo',
  fs,
  gitDirectory: '/path/to/repo/.git',
  gitCredentials: credentials,
  repoId: 'test-repo'
});

// Get current branch - returns correct value
const branch1 = await gitVCS.getCurrentBranch();
console.log(branch1); // 'main'

// Clone a different repo (or reinitialize)
await gitVCS.clone({
  url: 'https://github.com/example/other-repo',
  gitDirectory: '/path/to/other-repo/.git',
  // ... other options
});

// Get current branch again - still returns 'main' from the first repo
const branch2 = await gitVCS.getCurrentBranch();
console.log(branch2); // Still 'main', but should be the branch from the cloned repo
```

### Expected behavior

After performing operations like `init()` or `clone()`, the cached branch information should be invalidated so that `getCurrentBranch()` returns the actual current branch of the newly initialized/cloned repository, not the cached value from a previous operation.

The same issue appears to affect `getRemoteOriginURI()` as well - it returns cached values even after the repository context has changed.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
