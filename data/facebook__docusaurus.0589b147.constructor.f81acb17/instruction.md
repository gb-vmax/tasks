# Bug Report

### Describe the bug

When initializing a Git repository through the utility class, the initial commit setup is not working correctly. The repository ends up in an unexpected state where there's no proper initial commit, which causes issues with subsequent git operations that depend on having at least one commit in the history.

### Reproduction

```js
const git = new Git('/path/to/test/dir');
// Repository is initialized but the commit history is broken
// Subsequent operations that expect a commit to exist will fail
```

Steps to reproduce:
1. Initialize a new Git instance with a directory path
2. Try to perform operations that require an existing commit (like creating branches, checking out, etc.)
3. Operations fail because the initial commit wasn't created properly

### Expected behavior

The Git repository should be initialized with a proper first commit that can be used as a base for subsequent operations. The commit history should show exactly one initial commit after initialization.

### Additional context

This seems to have broken recently. The repository initialization completes without errors, but the commit state is not what's expected for a fresh repository with an initial commit.

---
Repository: /testbed
