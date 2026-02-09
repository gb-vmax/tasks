# Bug Report

### Describe the bug

The merge conflict schema appears to have syntax errors or malformed structure. When attempting to use the sync functionality, I'm encountering issues related to the `mergeConflictSchema` object definition.

### Reproduction

Looking at the schema definition in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`, the `mergeConflictSchema` object seems to have an invalid structure. The object properties don't follow the expected format.

When trying to work with merge conflicts in the sync module:

```js
import { mergeConflictSchema } from './type-schemas';

// Attempting to use the schema
const conflict = {
  mineBlob: mergeConflictSchema.mineBlob(),
  theirsBlobContent: mergeConflictSchema.theirsBlobContent(),
  // ... other properties
};
```

### Expected behavior

The `mergeConflictSchema` should be a valid schema object where all properties are properly defined as functions that return default values. The schema should be parseable and usable throughout the sync module without syntax errors.

### Additional context

This seems to affect the merge conflict resolution functionality. The schema definition should maintain a consistent structure across all properties.

---
Repository: /testbed
