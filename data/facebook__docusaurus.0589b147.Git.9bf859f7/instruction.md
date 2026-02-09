# Bug Report

### Describe the bug

The Git utility class is throwing errors when git operations succeed. When trying to initialize a git repository or commit changes, the operations complete successfully but the code throws an error anyway.

### Reproduction

```js
const git = new Git('/path/to/repo');
// This throws an error even though git init succeeded
```

Or when committing:

```js
const git = new Git('/path/to/repo');
git.commit('Initial commit', '2024-01-01', 'Test User <test@example.com>');
// Error is thrown before the commit actually executes
```

### Expected behavior

The Git class should only throw errors when git commands actually fail (non-zero exit code), not when they succeed. Successful git operations should complete without throwing exceptions.

### Additional context

This seems to affect both initialization and commit operations. The error messages indicate the operation failed, but checking the repository shows the commands actually executed successfully.

---
Repository: /testbed
