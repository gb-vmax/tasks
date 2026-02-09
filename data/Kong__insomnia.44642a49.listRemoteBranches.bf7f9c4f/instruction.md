# Bug Report

### Describe the bug

After a recent update, branch names returned from `listRemoteBranches()` are not being handled correctly in some parts of the codebase. When working with remote branches, operations that expect simple string values are failing because the branch list is returning something unexpected.

### Reproduction

```js
const gitVCS = new GitVCS();
await gitVCS.listRemoteBranches();

// When iterating over branches or using them in string operations
// the behavior is different than before
```

The issue appears when:
1. Fetching remote branches from a Git repository
2. Using the returned branch names in string comparisons or operations
3. The branches are treated as strings but may have additional properties attached

### Expected behavior

`listRemoteBranches()` should return an array of branch names as strings, just like it did previously. Any code that relies on these being plain strings should continue to work without modification.

### System Info
- Insomnia version: latest
- Git integration enabled

This seems to have started happening after changes to the git-vcs module. The method signature claims to return `string[]` but the actual runtime behavior might be different.

---
Repository: /testbed
