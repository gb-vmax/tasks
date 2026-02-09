# Bug Report

### Describe the bug

The VCS merge conflict handler seems to have been broken in a recent update. When attempting to pull changes that result in merge conflicts, the application throws an error instead of properly handling the conflicts.

### Reproduction

1. Set up a project with VCS enabled
2. Make conflicting changes on two different branches/clients
3. Attempt to pull/sync changes that would create merge conflicts
4. Application throws an error instead of allowing conflict resolution

### Expected behavior

The conflict handler should be invoked to allow the user to resolve merge conflicts interactively. Previously this worked fine, but now it appears the conflict resolution flow is completely broken.

### Additional context

This appears to have happened after some changes to the VCS conflict handling code. The error occurs during the pull operation when conflicts are detected. It seems like the code path that checks for and invokes the conflict handler may have been accidentally removed or corrupted.

---
Repository: /testbed
