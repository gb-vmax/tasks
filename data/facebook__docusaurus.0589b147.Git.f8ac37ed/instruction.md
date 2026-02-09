# Bug Report

### Describe the bug

I'm encountering an issue with the Git utility class where calling the `commit()` method results in an error about undefined variables. The method seems to be checking the results of git operations before they're actually executed.

### Reproduction

```js
const git = new Git();
git.init('/tmp/test-repo');
git.commit('Initial commit', '2024-01-01', 'Test User <test@example.com>');
```

This throws an error because `addRes` and `commitRes` are being referenced before they're defined.

### Expected behavior

The commit method should:
1. Execute `git add .` 
2. Execute `git commit` with the provided message, date, and author
3. Check the results of both operations for errors
4. Complete successfully if both operations succeed

### Additional context

This appears to affect the initialization sequence as well - the git config commands seem to be running in an unexpected order relative to the initial commit, though I'm not sure if that's related to the main issue.

---
Repository: /testbed
