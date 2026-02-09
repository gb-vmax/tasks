# Bug Report

### Describe the bug

After a recent update, the git branch listing functionality seems to be broken. When I try to view or switch branches in my workspace, the UI doesn't show all the branches that actually exist in my repository. Sometimes it shows branches that I've already deleted, and other times it's missing branches that definitely exist.

### Reproduction

1. Create a new workspace with git sync enabled
2. Create several branches (e.g., `feature-1`, `feature-2`, `main`)
3. Delete one of the branches locally using git CLI
4. Try to list branches in Insomnia
5. The deleted branch still appears in the list, or some existing branches are missing

It seems like the branch list is being cached or filtered incorrectly. The behavior is inconsistent - sometimes I see stale branches, sometimes fresh ones are missing.

### Expected behavior

The branch list should accurately reflect the current state of the repository:
- All existing branches should be displayed
- Deleted branches should not appear in the list
- The list should update properly when branches are added or removed

### System Info
- Insomnia version: latest
- OS: macOS
- Git version: 2.x

This is causing issues with my workflow as I can't reliably switch between branches or see what branches are available. Would appreciate a fix for this!

---
Repository: /testbed
