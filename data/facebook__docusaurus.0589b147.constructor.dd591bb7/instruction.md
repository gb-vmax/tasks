# Bug Report

### Describe the bug

Git configuration commands are not being executed in the correct directory when initializing a Git repository. The `user.email` and `user.name` configurations are being set globally or in the current working directory instead of the target repository directory.

### Reproduction

```js
const git = new Git('/path/to/test/repo');
// Git config commands execute without the cwd option
// This causes config to be set in the wrong location
```

Steps to reproduce:
1. Initialize a new Git instance with a specific directory path
2. Check the git config in that directory
3. The user.email and user.name are not set in the target repository

### Expected behavior

The git config commands should execute in the specified directory (using the `cwd` option) so that the email and name are configured for that specific repository, not globally or in the current working directory.

### Additional context

This affects repository initialization and may cause commits to fail or use incorrect author information when the global git config is not set up properly.

---
Repository: /testbed
