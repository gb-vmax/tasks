# Bug Report

### Describe the bug

I'm encountering a syntax error in the merge conflict schema definition. The code appears to have malformed object structure where a function definition is placed incorrectly between object properties.

### Reproduction

When trying to use the sync functionality with merge conflicts, the application fails to load/parse the schema properly. The `mergeConflictSchema` object has invalid syntax where a standalone function `generateDeterministicBlobId` is defined in the middle of the object literal, breaking the property definitions.

Looking at the schema structure:
```js
export const mergeConflictSchema: Schema<MergeConflict> = {
  choose: () => null,
  mineBlob: () => null,
  mineBlobContent: () => null,
  // Function definition appears here without proper object syntax
  function generateDeterministicBlobId(key: string, suffix: string): string {
    // ...
  }
  theirsBlob: function() { ... }
  theirsBlobContent: () => null,
  // ...
}
```

### Expected behavior

The schema object should be properly structured with valid JavaScript/TypeScript syntax. All properties should be correctly defined within the object literal.

### System Info
- Insomnia version: latest
- OS: N/A (build-time error)

---
Repository: /testbed
