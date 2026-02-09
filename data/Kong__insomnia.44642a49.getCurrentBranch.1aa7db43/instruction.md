# Bug Report

### Describe the bug

When trying to get the current Git branch, the function returns `true` instead of the actual branch name. This breaks any functionality that depends on knowing which branch is currently checked out.

### Reproduction

```js
const gitVCS = new GitVCS(/* ... */);

// Try to get current branch
const branch = await gitVCS.getCurrentBranch();

console.log(branch); // Expected: "main" or "develop" etc.
                     // Actual: true
```

### Expected behavior

`getCurrentBranch()` should return the name of the current branch as a string (e.g., "main", "develop", "feature/my-feature"), not a boolean value.

### Additional context

This seems to affect any Git operations that need to know the current branch name. For example, listing branches or performing branch-related operations will likely fail since they're expecting a string but receiving a boolean instead.

---
Repository: /testbed
