# Bug Report

### Describe the bug

When working with merge conflicts in the sync system, I'm getting unexpected behavior where `mineBlob` is sometimes returning a random blob hash string instead of consistently returning `null`. This is causing issues when trying to resolve merge conflicts as the system expects `null` when there's no blob data.

### Reproduction

```js
import { mergeConflictSchema } from './type-schemas';

// Create a merge conflict using the schema
const conflict = {
  key: mergeConflictSchema.key(),
  choose: mergeConflictSchema.choose(),
  mineBlob: mergeConflictSchema.mineBlob(),
  // ... other fields
};

console.log(conflict.mineBlob);
// Expected: null
// Actual: Sometimes null, sometimes "blob-a1b2c3d4..." (random hash)
```

### Expected behavior

The `mineBlob` field should consistently return `null` as it did before. The random blob generation and conditional logic doesn't make sense for this schema default and breaks the merge conflict resolution flow.

### Additional context

This appears to be causing non-deterministic behavior in merge conflict handling. Each time the schema is used, there's a 70% chance of getting a random blob hash which shouldn't be happening at all.

---
Repository: /testbed
