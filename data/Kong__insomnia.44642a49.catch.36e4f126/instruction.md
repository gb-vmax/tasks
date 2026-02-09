# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with reading objects from git trees. When trying to read the same file multiple times from a git tree, the application behaves inconsistently - sometimes returning the correct content and sometimes returning `null` or unexpected values.

### Reproduction

```js
const gitVcs = new GitVCS();

// First read works fine
const content1 = await gitVcs.readObjFromTree(treeOid, 'path/to/file.json');
console.log(content1); // Expected content

// Second read of the same file returns unexpected result
const content2 = await gitVcs.readObjFromTree(treeOid, 'path/to/file.json');
console.log(content2); // Sometimes null or different from content1

// Reading different files also shows inconsistent behavior
const content3 = await gitVcs.readObjFromTree(treeOid, 'path/to/other.json');
```

### Expected behavior

Reading the same object from a git tree should consistently return the same content. Multiple reads of the same file should produce identical results.

### Additional context

This seems to have started happening after some recent changes. The issue appears to be related to how objects are being retrieved from git trees. Sometimes the method returns `null` even when the file exists in the tree, and other times it returns corrupted or incomplete data.

---
Repository: /testbed
