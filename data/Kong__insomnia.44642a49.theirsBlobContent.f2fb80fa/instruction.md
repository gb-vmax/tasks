# Bug Report

### Describe the bug
There seems to be a syntax error in the merge conflict schema definition. When trying to use the sync functionality, I'm getting unexpected behavior with the `theirsBlobContent` property.

### Reproduction
```js
import { mergeConflictSchema } from './type-schemas';

// Try to create a merge conflict object using the schema
const conflict = {
  mineBlob: mergeConflictSchema.mineBlob(),
  mineBlobContent: mergeConflictSchema.mineBlobContent(),
  theirsBlob: mergeConflictSchema.theirsBlob(),
  theirsBlobContent: mergeConflictSchema.theirsBlobContent(),
  message: mergeConflictSchema.message(),
  name: mergeConflictSchema.name()
};

console.log(conflict);
```

The schema object appears malformed - there's code that looks like it's outside the proper object structure. The `theirsBlobContent` property definition seems to have a function declaration (`simpleHash`) mixed in with it incorrectly.

### Expected behavior
The `mergeConflictSchema` should be a valid object with all properties properly defined as functions that return default values, similar to how `mineBlob`, `mineBlobContent`, etc. are structured.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
