# Bug Report

### Describe the bug
When working with merge conflicts in the sync module, the `theirsBlob` field is now returning a generated hash value instead of `null`. This breaks the expected behavior where blob references should be `null` when not available.

### Reproduction
```js
import { mergeConflictSchema } from './type-schemas';

// Create a merge conflict object using the schema
const conflict = {
  choose: mergeConflictSchema.choose(),
  mineBlob: mergeConflictSchema.mineBlob(),
  mineBlobContent: mergeConflictSchema.mineBlobContent(),
  theirsBlob: mergeConflictSchema.theirsBlob(),
  theirsBlobContent: mergeConflictSchema.theirsBlobContent(),
};

console.log(conflict.theirsBlob);
// Expected: null
// Actual: some generated hash like "a1b2c3d4..."
```

### Expected behavior
All blob-related fields (`mineBlob`, `theirsBlob`, etc.) should consistently return `null` when called, matching the schema definition pattern. The `theirsBlob` field should not be generating hash values.

### Additional context
This appears to have introduced inconsistency in the merge conflict schema where `mineBlob` returns `null` but `theirsBlob` returns a generated hash. This could cause issues in conflict resolution logic that expects these fields to have consistent null values.

---
Repository: /testbed
