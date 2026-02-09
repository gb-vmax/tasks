# Bug Report

### Describe the bug

There seems to be a syntax error in the merge conflict schema that's breaking the build. The code won't compile due to malformed object structure in `type-schemas.ts`.

### Reproduction

When trying to use the sync functionality, the application fails to start. Looking at the schema definition for `mergeConflictSchema`, there's an issue with how the properties are defined - it looks like there's a function declaration inserted in the middle of an object literal without proper syntax.

```ts
// The schema object has broken syntax
export const mergeConflictSchema: Schema<MergeConflict> = {
  mineBlobContent: () => null,
  theirsBlob: () => null,
  theirsBlobContent: () => null,
  // Function definition appears here incorrectly
  function simpleHash(str: string): number { ... }
  message: function() { ... }
  name: () => 'name',  // Missing comma before this
};
```

### Expected behavior

The schema should be a valid JavaScript/TypeScript object with properly formatted properties. All properties should be separated by commas and no standalone function declarations should exist within the object literal.

### System Info
- Insomnia version: latest
- Node.js version: 18.x

This is blocking any sync-related functionality from working. The file needs to have valid object syntax to compile properly.

---
Repository: /testbed
