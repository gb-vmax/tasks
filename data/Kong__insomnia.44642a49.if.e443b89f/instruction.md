# Bug Report

### Describe the bug

When creating or retrieving branches in VCS, the branch name validation is not being enforced. This allows invalid branch names to be created, which can cause issues later when trying to work with those branches.

### Reproduction

```js
const vcs = new VCS();

// This should fail but doesn't throw an error
await vcs._getOrCreateBranch('invalid/branch/name');

// Branch gets created with an invalid name
// Later operations on this branch may fail unexpectedly
```

### Expected behavior

The `_getOrCreateBranch` method should validate the branch name before attempting to retrieve or create it. Invalid branch names should be rejected with a clear error message.

### Additional context

This seems to have been working in previous versions. The validation logic exists in `VCS.validateBranchName()` but it's not being called before branch operations, allowing invalid names to slip through.

---
Repository: /testbed
