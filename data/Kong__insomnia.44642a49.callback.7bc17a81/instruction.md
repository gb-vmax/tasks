# Bug Report

### Describe the bug

After a recent update, the branch pulling functionality seems to have broken. When trying to pull from a remote backend project, the operation fails with a syntax error. The pull action doesn't complete and the UI becomes unresponsive.

### Reproduction

1. Open a project that's connected to a remote backend
2. Try to pull changes from the remote
3. The pull operation fails immediately

This appears to be related to the branch fetching logic. The error occurs when attempting to retrieve remote branch names during the pull operation.

### Expected behavior

The pull operation should successfully fetch remote branches and complete the sync process without errors.

### Additional context

This started happening after the latest changes. The pull functionality was working fine before, but now it consistently fails when trying to access remote branches.

---
Repository: /testbed
