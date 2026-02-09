# Bug Report

### Describe the bug

I'm experiencing an issue with branch creation in the VCS module. When I try to create or retrieve a branch, the operation seems to hang or behave unexpectedly. The branch name handling appears to have changed, and now branches with different casing or whitespace are being treated as the same branch.

### Reproduction

```js
// Create a branch with uppercase name
await vcs._getOrCreateBranch('MyFeature');

// Try to get a branch with lowercase name
await vcs._getOrCreateBranch('myfeature');

// These now seem to refer to the same branch, which wasn't the case before
```

Also, when creating new branches, they seem to inherit snapshots from the current branch, which is causing unexpected behavior in our workflow.

### Expected behavior

- Branch names should be treated as case-sensitive (or at least preserve the original casing)
- Different variations of branch names (with/without whitespace) should be treated as distinct branches
- New branches should start with an empty snapshot history unless explicitly specified

### System Info
- Insomnia version: latest
- OS: macOS

This started happening recently and is breaking our branch management workflow. Any help would be appreciated!

---
Repository: /testbed
