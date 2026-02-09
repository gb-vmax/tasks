# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict resolution where the `mineBlobContent` is always returning `null` instead of the actual blob content. This is preventing me from viewing or resolving merge conflicts properly in the UI.

### Reproduction

```js
const conflict = {
  key: 'some-key',
  mineBlob: {
    name: 'My Request',
    description: 'Test description',
    method: 'GET'
  }
};

// Try to get the blob content
const content = mergeConflictSchema.mineBlobContent(conflict.mineBlob);
// Expected: some string representation of the blob
// Actual: null
```

### Expected behavior

When there's actual content in the blob object, `mineBlobContent` should return a string representation of that content so it can be displayed in the merge conflict resolution interface. Currently it's just returning `null` even when the blob contains valid data.

### Additional context

This seems to affect the merge conflict UI where users need to see the differences between conflicting versions. Without being able to see the content, it's impossible to make informed decisions about which version to keep.

---
Repository: /testbed
