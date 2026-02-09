# Bug Report

### Describe the bug

I'm experiencing an issue with the VCS conflict handling system. After a recent update, the code appears to be incomplete and causes the application to crash when merge conflicts are encountered.

When attempting to merge branches or pull changes that result in conflicts, the application throws an error and the merge operation fails completely. This is blocking our ability to sync changes across team members.

### Reproduction

1. Create a project with version control enabled
2. Make conflicting changes in two different branches/locations
3. Attempt to merge or pull the changes
4. The application crashes instead of handling the conflicts

### Expected behavior

The conflict handler should be invoked to resolve merge conflicts, either automatically or by prompting the user. The merge operation should complete successfully after conflicts are resolved.

### Additional context

This seems to have started happening recently. The conflict resolution flow was working fine before, but now it just errors out. It looks like something might be incomplete in the conflict handling logic.

---
Repository: /testbed
