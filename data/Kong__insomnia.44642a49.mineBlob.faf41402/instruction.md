# Bug Report

### Describe the bug
When working with merge conflicts, the `mineBlob` field is not being generated correctly. It appears that the blob hash is always returning `null` instead of generating a proper hash value when there's actual content in the merge conflict.

### Reproduction
```js
const mergeConflict = {
  key: 'conflict-key',
  choose: 'mine',
  mineBlobContent: 'some content',
  theirsBlob: null,
  theirsBlobContent: null
}

// Expected: mineBlob should contain a hash value
// Actual: mineBlob is null
```

### Expected behavior
When `mineBlobContent` is not null or when `choose` is set, the `mineBlob` field should generate and return a proper blob hash string (40 character hex string), not `null`.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with sync functionality where merge conflicts aren't being tracked properly because the blob references are missing.

---
Repository: /testbed
