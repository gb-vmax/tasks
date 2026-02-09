# Bug Report

### Describe the bug
When calling `getCurrentBranch()`, the method returns an unexpected object instead of the branch name string. This breaks any code that depends on getting the current branch name.

### Reproduction
```js
const gitVCS = new GitVCS(/* ... */);

// Try to get current branch name
const branchName = await gitVCS.getCurrentBranch();

console.log(branchName); // Expected: "main" or "develop" etc.
console.log(typeof branchName); // Expected: "string"
// Actual: returns an object instead of branch name string
```

### Expected behavior
`getCurrentBranch()` should return the current branch name as a string (e.g., "main", "develop", "feature/xyz"). Instead, it's returning an object which causes issues when trying to use the branch name for operations like listing branches or displaying the current branch in the UI.

### Additional context
This seems to have broken recently. The method used to work correctly and return the branch name string, but now it's returning something else entirely. Any code that calls `getCurrentBranch()` and expects a string will fail.

---
Repository: /testbed
