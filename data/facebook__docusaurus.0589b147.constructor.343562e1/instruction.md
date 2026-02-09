# Bug Report

### Describe the bug

After a recent update, Git repository initialization is failing silently in the test utilities. When creating a new Git instance, the repository appears to be created but doesn't have any initial commit, which causes subsequent git operations to fail with errors like "fatal: your current branch 'master' does not have any commits yet".

### Reproduction

```js
const git = new Git('/path/to/test/dir');
// Try to perform any git operation that requires a commit history
git.commit('Test commit', '2024-01-01', 'Author');
// This fails because there's no initial commit to build on
```

### Expected behavior

The Git utility should initialize a repository with an initial empty commit so that subsequent operations work correctly. Previously this was working fine and all git operations could be performed immediately after initialization.

### System Info
- Node version: 18.x
- shelljs version: latest

---
Repository: /testbed
