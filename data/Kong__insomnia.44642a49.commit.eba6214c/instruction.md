# Bug Report

### Describe the bug

After a recent update, the git commit functionality is breaking when trying to commit changes. The commit operation now throws an error about "No changes to commit" even when there are clearly modified files in the working directory that haven't been staged yet.

### Reproduction

```js
// Modify a tracked file
await vcs.writeFile('test.json', JSON.stringify({ foo: 'bar' }));

// Try to commit without explicitly staging
await vcs.commit('Update test file');
// Error: No changes to commit
```

### Expected behavior

The commit should work automatically with modified tracked files, or at least not throw an error when there are unstaged changes. Previously this was working fine and would just create the commit.

### Additional context

This seems to have started happening after the latest changes to the git-vcs module. The commit method now checks for staged changes and tries to auto-stage files, but something in the logic isn't working correctly. It's detecting that there are no staged changes, but then also not finding the modified files to stage them.

The status checking logic might not be matching the file statuses correctly - it's looking for statuses that end with '0' or start with '1', and also checking for '*modified', but I'm not sure these match what's actually being returned by the status method.

---
Repository: /testbed
