# Bug Report

### Describe the bug
When setting git author information, the config scope is being incorrectly determined, causing author settings to be written to the wrong location (global vs local repository config). This results in author information not being properly saved or applied to commits.

### Reproduction
```js
const gitVcs = new GitVCS();

// Try to set author for a repository
await gitVcs.setAuthor('John Doe', 'john@example.com');

// The author config gets written with an incorrect scope prefix
// Expected: writes to local repo config when gitdir is set
// Actual: writes to global config or with wrong path
```

### Expected behavior
- When a git directory is configured (`gitdir` is set in `_baseOpts`), author settings should be written to the local repository config without any scope prefix
- When no git directory is configured, author settings should be written to global config with the `global.` prefix
- The config paths should be `user.name` and `user.email` (or `global.user.name` and `global.user.email` for global scope)

### Current behavior
The scope determination logic appears to be inverted - it returns an empty string when `gitdir` exists and `'global.'` when it doesn't, which is backwards from what's needed.

This causes commits to either fail to use the correct author information or write config to the wrong location entirely.

---
Repository: /testbed
