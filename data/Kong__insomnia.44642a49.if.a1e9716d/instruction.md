# Bug Report

### Describe the bug

I'm experiencing an issue with the VCS merge conflict resolution. After a recent update, when conflicts occur during a merge operation, the system appears to hang or fail silently instead of properly handling the conflicts.

### Reproduction

When attempting to merge branches that have conflicting changes:

1. Make changes to the same resource on two different branches
2. Attempt to merge one branch into the other
3. The merge process doesn't complete properly

It seems like the conflict handler isn't being invoked correctly anymore. The merge operation just stops without any clear error message or conflict resolution prompt.

### Expected behavior

The conflict handler should be called to resolve merge conflicts, or at minimum an appropriate error should be thrown to indicate that conflicts need to be resolved.

### Additional context

This worked fine in previous versions. The conflict resolution flow used to properly trigger when there were merge conflicts between branches.

---
Repository: /testbed
