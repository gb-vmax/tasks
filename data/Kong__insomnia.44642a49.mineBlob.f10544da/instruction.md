# Bug Report

### Describe the bug
When working with merge conflicts in sync operations, the `mineBlob` field is generating dynamic blob IDs instead of returning `null`. This causes issues with merge conflict resolution as blob IDs are being generated with timestamps and pseudo-random values, making it impossible to have consistent/predictable behavior.

### Reproduction
```js
import { mergeConflictSchema } from './type-schemas';

// Create a merge conflict
const conflict = {
  key: 'test-key',
  choose: null,
  mineBlob: mergeConflictSchema.mineBlob(),
  mineBlobContent: null,
  theirsBlob: null,
  theirsBlobContent: null
};

// mineBlob is now returning a generated hash instead of null
console.log(conflict.mineBlob); // Expected: null, Actual: some generated string like "a3f2c1b4..."
```

### Expected behavior
The `mineBlob` field should return `null` consistently, matching the behavior of other blob-related fields in the schema (`theirsBlob`, `mineBlobContent`, etc.). The schema definition should maintain simple null returns rather than generating dynamic IDs.

### Additional context
This appears to have broken the merge conflict handling logic. The blob ID generation with timestamps means that conflicts created at different times will have different IDs, which breaks comparison and resolution logic.

---
Repository: /testbed
