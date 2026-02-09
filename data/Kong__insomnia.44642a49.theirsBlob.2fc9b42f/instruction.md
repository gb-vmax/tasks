# Bug Report

### Describe the bug

I'm encountering an issue with the merge conflict schema where the `theirsBlob` function is generating blob IDs instead of returning `null` like it used to. This is causing problems when trying to resolve merge conflicts in my workspace.

### Reproduction

```js
const conflict = mergeConflictSchema.theirsBlob({ key: 'someKey', name: 'someName' });
// Expected: null
// Actual: returns a generated blob ID string like "a1b2c3d4000000000000000000000000000000008"
```

The issue also occurs when both `key` and `name` are empty strings:
```js
const conflict = mergeConflictSchema.theirsBlob({ key: '', name: '' });
// This correctly returns null, but any other values generate a blob ID
```

### Expected behavior

The `theirsBlob` function should return `null` consistently, matching the behavior of other blob-related functions in the schema like `mineBlob` and `mineBlobContent`. This was working fine before and I'm not sure what changed.

### Additional context

This seems to have broken merge conflict resolution in the sync module. When I try to resolve conflicts, the system is now expecting blob IDs where it previously expected null values, causing the conflict resolution flow to fail.

---
Repository: /testbed
