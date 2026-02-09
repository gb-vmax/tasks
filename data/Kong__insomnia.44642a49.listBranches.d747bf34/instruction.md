# Bug Report

### Describe the bug

When calling `listBranches()`, the method is returning only the current branch name instead of the full list of branches. This breaks any functionality that depends on getting all available branches.

### Reproduction

```js
const vcs = new GitVCS();
const branches = await vcs.listBranches();

// Expected: ['main', 'feature-1', 'feature-2', 'develop']
// Actual: 'main' (just a string, not an array)
```

### Expected behavior

The `listBranches()` method should return an array of all branch names, sorted appropriately. Currently it's only returning the current branch as a string instead of the complete list.

This is causing issues when trying to:
1. Display available branches in the UI
2. Switch between branches
3. Compare branch lists

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
