# Bug Report

### Describe the bug

When using the Git utility class to create commits, the commit date is not being set correctly. The `GIT_COMMITTER_DATE` environment variable is missing, which means commits are being created with the current timestamp instead of the specified date.

### Reproduction

```js
const git = new Git();
git.commit('test message', '2024-01-15', 'Test Author <test@example.com>');

// The commit is created but with the wrong date
// Expected: 2024-01-15T00:00:00Z
// Actual: Current system time
```

### Expected behavior

Commits should be created with both the author date and committer date set to the specified date parameter. The `--date` flag sets the author date, but the committer date should also be controlled via the `GIT_COMMITTER_DATE` environment variable.

### Additional context

This affects any functionality that relies on consistent commit timestamps, such as changelog generation or git history analysis tools.

---
Repository: /testbed
