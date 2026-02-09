# Bug Report

### Describe the bug
When trying to get the current Git branch, I'm getting an error saying "No active branch" even though I'm clearly on a valid branch. This seems to be happening consistently whenever I try to interact with Git operations in Insomnia.

### Reproduction
1. Set up a Git repository with Insomnia sync
2. Make sure you're on a valid branch (e.g., `main` or `master`)
3. Try to perform any Git operation that requires getting the current branch
4. Error is thrown: "No active branch"

### Expected behavior
The current branch name should be returned successfully when on a valid branch. The error should only be thrown when there actually is no active branch (like in a detached HEAD state).

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my ability to use Git sync features. Any workaround would be appreciated!

---
Repository: /testbed
