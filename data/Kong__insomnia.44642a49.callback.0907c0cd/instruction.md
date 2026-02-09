# Bug Report

### Describe the bug

I'm experiencing an issue with branch synchronization where remote branches are being cached and not reflecting the actual state of the remote repository. When pulling a backend project, the system returns stale branch information even after new branches have been created or deleted on the remote.

### Reproduction

Steps to reproduce:
1. Create a backend project and sync it with a remote repository
2. Pull the project to get the list of remote branches
3. Add a new branch on the remote repository
4. Pull the project again within 5 minutes
5. The newly created remote branch is not visible

The branch list appears to be cached and doesn't update even when the remote state has changed. This causes issues when trying to switch to or work with recently created branches.

### Expected behavior

Each pull operation should fetch the current state of remote branches from the repository, not return cached data. The branch list should always reflect the actual remote state.

### Additional context

This seems to happen consistently when pulling projects multiple times in quick succession. The cached branch information persists for several minutes, which makes it difficult to work with rapidly changing remote repositories.

---
Repository: /testbed
