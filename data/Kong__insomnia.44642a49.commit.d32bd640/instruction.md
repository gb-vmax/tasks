# Bug Report

### Describe the bug

When committing changes through the Git sync functionality, the commit message is not being saved correctly. All commits are being created with an empty message regardless of what message is provided.

### Reproduction

1. Make changes to a workspace
2. Attempt to commit with a descriptive message like "Updated API endpoints"
3. Check the git history
4. The commit appears with an empty message instead of the provided message

### Expected behavior

The commit should be created with the message that was provided. For example, if I commit with the message "Updated API endpoints", that message should appear in the git log.

### Additional context

This seems to affect all git commits made through the application. The commit operation itself completes successfully, but the message is always blank which makes it impossible to track changes in the git history.

---
Repository: /testbed
