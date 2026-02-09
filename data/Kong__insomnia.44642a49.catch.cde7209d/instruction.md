# Bug Report

### Describe the bug

After a recent update, the Git sync functionality appears to be broken. When trying to read objects from the Git tree, the operation fails silently and returns `null` instead of the expected object data. This is affecting the ability to pull changes from remote repositories.

### Reproduction

1. Set up a project with Git sync enabled
2. Try to read an object from a Git tree using a valid tree OID and file path
3. The operation returns `null` even though the object exists in the repository

Example scenario:
```js
// Attempting to read a file from the Git tree
const treeOid = 'abc123...'; // valid tree OID
const filePath = 'path/to/file.json';
const result = await gitVcs.readObjFromTree(treeOid, filePath);
// Expected: file contents
// Actual: null
```

### Expected behavior

The `readObjFromTree` method should successfully retrieve objects from the Git tree and return their contents. It should only return `null` when the object genuinely doesn't exist in the tree, not when there are transient errors.

### Additional context

This seems to have started happening after the latest changes. The Git operations appear to be failing without proper error handling, making it difficult to sync with remote repositories. The sync process just silently fails without any indication of what went wrong.

---
Repository: /testbed
