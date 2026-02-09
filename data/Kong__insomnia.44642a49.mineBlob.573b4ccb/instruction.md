# Bug Report

### Describe the bug

After a recent update, I'm getting errors when trying to work with merge conflicts in the sync module. The application crashes with `TypeError: this.getBlobQueue is not a function` when attempting to resolve merge conflicts.

### Reproduction

```js
const conflict = {
  key: 'some-key',
  choose: null,
  mineBlob: mergeConflictSchema.mineBlob,
  mineBlobContent: null,
  theirsBlob: null,
  theirsBlobContent: null,
};

// This throws an error
const blob = conflict.mineBlob();
```

### Expected behavior

The `mineBlob` function should return `null` or a valid blob object without throwing errors. Previously this was working fine and would just return `null` when there was no blob data.

### Additional context

This seems to have started happening recently. The error occurs when the sync system tries to process merge conflicts. The function is trying to call methods like `getBlobQueue()`, `isValidBlob()`, `getMaxBlobSize()`, etc. that don't exist in the context where it's being called.

---
Repository: /testbed
