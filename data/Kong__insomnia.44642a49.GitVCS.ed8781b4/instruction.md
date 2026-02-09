# Bug Report

### Describe the bug

After recent changes, I'm getting an error when trying to use GitVCS methods without properly initializing the repository first. The error message says "GitVCS not initialized. Call init() or initFromClone() first."

### Reproduction

```js
const gitVCS = new GitVCS();

// Set up base options but don't call init() or initFromClone()
gitVCS._baseOpts = {
  repoId: 'my-repo-id',
  // ... other options
};

// Try to use any git operation
await gitVCS.listFiles();
// Error: GitVCS not initialized. Call init() or initFromClone() first.
```

This also happens with other methods like:
- `getCurrentBranch()`
- `listBranches()`
- `listRemoteBranches()`
- `fetchRemoteBranches()`
- `status()`

### Expected behavior

Previously, these methods would work as long as the base options were set up correctly. Now they require explicit initialization through `init()` or `initFromClone()`, but this breaks existing code that was setting up the GitVCS instance in other ways.

### Additional context

This seems to have started happening recently. Our workflow creates GitVCS instances and configures them manually without always calling the init methods, and now those operations are failing with this error.

Is there a way to use these methods without going through init/initFromClone? Or do we need to refactor all our code to use the initialization methods?

---
Repository: /testbed
