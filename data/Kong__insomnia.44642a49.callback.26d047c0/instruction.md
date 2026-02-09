# Bug Report

### Describe the bug

After a recent update, the branch pulling functionality appears to be broken. When trying to pull a backend project, the operation fails with a syntax error. The application becomes unresponsive when attempting to sync with remote branches.

### Reproduction

1. Open a project that's connected to a backend/remote repository
2. Attempt to pull changes from the remote
3. The pull operation fails immediately

This seems to affect all projects, not just specific ones. The issue started appearing after the latest changes to the VCS pull logic.

### Expected behavior

The pull operation should successfully fetch remote branch information and complete without errors. The branch list should be retrieved and cached properly for subsequent operations.

### Additional context

The problem appears to be related to the remote branch fetching mechanism. Previously working projects now fail to sync. Rolling back to an earlier version resolves the issue temporarily.

---
Repository: /testbed
