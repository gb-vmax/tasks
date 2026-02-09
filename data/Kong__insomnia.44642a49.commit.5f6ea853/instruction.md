# Bug Report

### Describe the bug

I'm experiencing an issue with git commits where the commit messages are being truncated unexpectedly. When I try to commit changes with a descriptive message, only the first few characters appear in the git history.

### Reproduction

```js
// Attempting to commit with a normal commit message
await gitVCS.commit("Fixed authentication bug in user login flow");

// Expected: Full message in git log
// Actual: Only "Fixed auth" appears in the commit history
```

When I check the git log after committing, the message is cut off at 10 characters instead of preserving the full commit message. This makes it really difficult to understand what changes were made when reviewing the git history.

### Expected behavior

The full commit message should be preserved in the git history. Commit messages are important for documentation and should not be truncated.

### Additional context

This seems to have started happening recently. I'm using the Git sync feature and all my commit messages are being shortened, which is breaking our workflow since we rely on descriptive commit messages for tracking changes.

---
Repository: /testbed
