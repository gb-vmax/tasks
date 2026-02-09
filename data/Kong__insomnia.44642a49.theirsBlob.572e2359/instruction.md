# Bug Report

### Describe the bug

After a recent update, I'm encountering a syntax error in the merge conflict schema file. The code appears to have malformed structure where function definitions are mixed with object property definitions in an unexpected way.

### Reproduction

When trying to use the sync functionality with merge conflicts, the application fails to load properly. The issue seems to be in the `mergeConflictSchema` object definition where new blob generation logic was added.

Looking at the schema definition:
```js
export const mergeConflictSchema: Schema<MergeConflict> = {
  choose: () => null,
  mineBlob: () => null,
  mineBlobContent: () => null,
  // ... code appears broken here
  theirsBlob: () => generateBlobId('theirs'),
  theirsBlobContent: () => null,
  // ...
}
```

The structure of the object seems corrupted - there are standalone function declarations and variable initializations appearing in the middle of what should be an object literal.

### Expected behavior

The schema object should be properly formatted with all properties correctly defined. The application should load without syntax errors and merge conflict handling should work as expected.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

This is blocking our ability to use the sync feature. Any help would be appreciated!

---
Repository: /testbed
