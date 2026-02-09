# Bug Report

### Describe the bug

After a recent update, the branch synchronization feature seems to have broken. When trying to pull from a remote project, the application hangs or becomes unresponsive. This appears to be related to how remote branches are being fetched.

### Reproduction

1. Open a project that's connected to a remote backend
2. Attempt to pull changes from the remote project
3. The pull operation doesn't complete and the UI becomes unresponsive

This was working fine before the latest changes. It seems like something is preventing the remote branch fetch from completing properly.

### Expected behavior

The pull operation should complete successfully and fetch the latest changes from the remote project without hanging.

### Additional context

This happens consistently with all my projects that have remote backends configured. The issue appears immediately when initiating a pull operation.

---
Repository: /testbed
