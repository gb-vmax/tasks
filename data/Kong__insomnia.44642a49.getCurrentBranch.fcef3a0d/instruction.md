# Bug Report

### Describe the bug

The `getCurrentBranch()` method is returning a boolean value instead of the actual branch name string. This breaks any code that expects to receive the branch name for display or comparison purposes.

### Reproduction

```js
const gitVcs = new GitVCS(/* ... */);

// This should return the branch name like "main" or "develop"
const currentBranch = await gitVcs.getCurrentBranch();

console.log(currentBranch); // Expected: "main", Actual: true
console.log(typeof currentBranch); // Expected: "string", Actual: "boolean"
```

### Expected behavior

`getCurrentBranch()` should return the name of the current branch as a string (e.g., "main", "develop", "feature/xyz"), not a boolean value.

### Impact

This affects:
- Branch name display in the UI
- Branch comparison logic
- Any downstream code that relies on the branch name string

### System Info
- Insomnia version: latest
- Git integration enabled

---
Repository: /testbed
