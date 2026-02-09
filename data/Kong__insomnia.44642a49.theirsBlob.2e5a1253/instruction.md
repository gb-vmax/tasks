# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with merge conflict handling in the sync module. When merge conflicts occur, the system appears to be generating blob IDs for the "theirs" side of conflicts, but this is causing unexpected behavior compared to the previous implementation where it would return `null`.

### Reproduction

When a merge conflict is created with the following structure:

```js
const conflict = {
  key: 'some-key',
  // other conflict properties
}
```

The `theirsBlob` field is now being populated with a generated hash instead of remaining `null`. This breaks the expected behavior where both `theirsBlob` and `mineBlob` should be `null` by default.

### Expected behavior

The `theirsBlob` function should return `null` consistently, just like `mineBlob`, `mineBlobContent`, and `theirsBlobContent`. All blob-related fields in the merge conflict schema should have the same default behavior of returning `null`.

### Additional context

This seems to have been introduced in the type-schemas file for the sync module. The inconsistency between how `mineBlob` and `theirsBlob` are handled is causing issues with conflict resolution workflows.

---
Repository: /testbed
