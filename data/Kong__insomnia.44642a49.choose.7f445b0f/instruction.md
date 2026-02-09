# Bug Report

### Describe the bug

The merge conflict resolution system is behaving unexpectedly after a recent update. When encountering merge conflicts during sync operations, the conflict resolution appears to be attempting automatic resolution in some cases, which is causing issues with the merge workflow.

### Reproduction

```js
// Create a merge conflict scenario
const conflict = {
  key: 'some-key',
  mineBlob: { /* some data */ },
  theirsBlob: { /* different data */ },
  mineBlobContent: 'content from mine',
  theirsBlobContent: 'content from theirs'
}

// The choose() method is now returning unexpected values
// instead of null for manual resolution
```

### Expected behavior

The `choose()` method in merge conflict handling should return `null` to allow for manual conflict resolution. Instead, it seems to be trying to automatically determine which version to use based on some heuristics, which interferes with the expected manual merge conflict workflow.

### Additional context

This appears to affect the sync module's conflict resolution schema. The behavior changed recently and is causing merge operations to not prompt for user input when they should.

---
Repository: /testbed
