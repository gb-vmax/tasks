# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with fetching remote Git branches. The application seems to be returning cached/stale branch data even when the remote repository has been updated with new branches or branch deletions.

### Reproduction

1. Set up a Git repository with remote branches
2. Call `fetchRemoteBranches()` to get the list of remote branches
3. Add or delete a branch on the remote repository
4. Call `fetchRemoteBranches()` again within a few minutes
5. The returned branch list still shows the old branches instead of the updated list

### Expected behavior

The method should always return the current state of remote branches, or at minimum there should be a way to force a refresh when needed. Right now it seems like once the branches are cached, there's no way to get fresh data even if I know the remote has changed.

### Additional context

This is particularly problematic when working in a team environment where branches are frequently created and deleted. The UI shows branches that no longer exist or doesn't show newly created branches until some timeout period expires.

Is there a way to bypass the cache or force a refresh? I don't see any options exposed for this in the current implementation.

---
Repository: /testbed
