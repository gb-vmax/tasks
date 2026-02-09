# Bug Report

### Describe the bug

After a recent update, the `add()` method in git-vcs is not working as expected when called with a single file path. The method appears to have changed its return behavior - it now returns `undefined` instead of the expected result when adding a single file.

### Reproduction

```js
const gitVcs = new GitVCS();

// This used to return a result, but now returns undefined
const result = await gitVcs.add('path/to/file.json');

console.log(result); // undefined (unexpected)
```

### Expected behavior

When calling `add()` with a single file path string, it should return a result (similar to the isomorphic-git library's behavior) or at least maintain the same return type as before. The method seems to have introduced conditional return logic that breaks existing code expecting a consistent return value.

### Additional context

This is causing issues in our workflow where we need to check the result of the add operation. The method now returns different types depending on whether the input is a string or array, which wasn't the case before.

---
Repository: /testbed
