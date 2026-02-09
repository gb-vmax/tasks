# Bug Report

### Describe the bug

I'm experiencing an issue with branch creation in VCS where providing a valid branch name throws an error saying "No branch name specified for get-or-create operation". This is preventing me from creating or switching to branches with non-empty names.

### Reproduction

```js
// Attempting to create or get a branch with a valid name
await vcs._getOrCreateBranch('feature-branch')
// Error: No branch name specified for get-or-create operation

// This also fails
await vcs._getOrCreateBranch('main')
// Error: No branch name specified for get-or-create operation
```

### Expected behavior

When calling `_getOrCreateBranch()` with a valid, non-empty branch name like `'feature-branch'` or `'main'`, it should either retrieve the existing branch or create a new one. The error should only be thrown when the name is actually empty or undefined.

### Additional context

This seems to have broken recently - I was able to create branches normally before. Now any branch name I provide triggers the validation error, making it impossible to work with branches at all.

---
Repository: /testbed
