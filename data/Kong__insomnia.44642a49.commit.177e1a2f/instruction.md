# Bug Report

### Describe the bug
When committing changes using the git sync functionality, only the first character of the commit message is being saved instead of the full message. This causes commit messages to be truncated to a single character.

### Reproduction
```js
// Attempt to commit with a meaningful message
await gitVCS.commit("Add new API endpoint for user authentication");

// Expected: Full commit message is saved
// Actual: Only "A" is saved as the commit message
```

### Steps to reproduce:
1. Make changes to your workspace
2. Attempt to commit with a descriptive message (e.g., "Update request headers")
3. Check the git log/history
4. Observe that only the first character of the message appears

### Expected behavior
The full commit message should be preserved and stored in the git history, not just the first character.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

This is making it really difficult to track changes since all commit messages are now single letters. Would appreciate a fix for this!

---
Repository: /testbed
