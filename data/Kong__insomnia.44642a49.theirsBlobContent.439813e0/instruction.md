# Bug Report

### Describe the bug

I'm experiencing an issue with the sync schema definitions where the `theirsBlobContent` property appears to be corrupted or malformed. When trying to use merge conflict resolution functionality, I'm getting unexpected behavior that seems related to the schema definition.

### Reproduction

```typescript
import { mergeConflictSchema } from './type-schemas';

// Try to create a merge conflict object
const conflict = {
  key: 'test-key',
  message: 'Conflict detected',
  mineBlob: null,
  mineBlobContent: null,
  theirsBlob: null,
  theirsBlobContent: null,
};

// When accessing the schema, something seems wrong with theirsBlobContent
console.log(mergeConflictSchema.theirsBlobContent);
// Expected: a function that returns null
// Actual: undefined or malformed function
```

### Expected behavior

The `theirsBlobContent` property in the merge conflict schema should be a simple function that returns `null`, just like the other blob-related properties (`mineBlob`, `mineBlobContent`, `theirsBlob`). The schema should be properly closed and all properties should be accessible.

### Additional context

This seems to have broken after a recent change. The merge conflict resolution feature is not working as expected, and I suspect it's related to how the schema is defined. Looking at the schema object, it appears the structure might be incomplete or corrupted.

---
Repository: /testbed
