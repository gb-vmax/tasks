# Bug Report

### Describe the bug

When listing Git branches, the current branch is being duplicated in the list when it already exists. Additionally, the branch list appears to be sorted incorrectly.

### Reproduction

```js
// Initialize a git repository with existing branches
const gitVcs = new GitVCS();

// Create and checkout a branch (e.g., 'main')
await gitVcs.checkout({ branch: 'main' });

// List branches
const branches = await gitVcs.listBranches();

// Expected: ['main', 'feature-branch', 'develop']
// Actual: ['main', 'main', 'feature-branch', 'develop']
```

### Steps to reproduce:
1. Initialize a git repository with at least one branch
2. Checkout an existing branch
3. Call `listBranches()`
4. The current branch appears twice in the returned list

### Expected behavior

The branch list should contain each branch exactly once, with no duplicates. The current branch should be included in the list only if it wasn't already there.

### Additional context

This seems to happen specifically when the current branch already exists in the branches array returned by `git.listBranches()`. The original behavior was meant to handle fresh repos with no commits where the current branch might not be listed, but now it's adding duplicates for normal cases.

---
Repository: /testbed
