# Bug Report

### Describe the bug

After a recent update, git commits are failing with an error. When trying to commit changes through the sync interface, I'm getting unexpected behavior where the commit operation doesn't work as expected.

### Reproduction

1. Make changes to a project that's synced with git
2. Try to commit the changes with a commit message
3. The commit fails or behaves unexpectedly

It seems like the commit message isn't being passed correctly to the underlying git operation. The commit function appears to be spreading the message string directly into the options object instead of passing it as the `message` property.

### Expected behavior

The commit should succeed with the provided commit message, and the changes should be committed to the git repository.

### System Info
- Insomnia version: latest
- OS: (platform independent issue)

---
Repository: /testbed
