# Bug Report

### Describe the bug

Entry point chunks are being skipped during bundle name reservation, causing some entry chunks to not have their names properly reserved. This results in potential naming conflicts or missing preliminary file names for user-defined entry points.

### Reproduction

```js
// Create a bundle with multiple entry points
const chunks = [
  { facadeModule: { isUserDefinedEntryPoint: true }, getPreliminaryFileName: () => 'entry1.js' },
  { facadeModule: { isUserDefinedEntryPoint: true }, getPreliminaryFileName: () => 'entry2.js' },
  { facadeModule: { isUserDefinedEntryPoint: true }, getPreliminaryFileName: () => 'entry3.js' },
  { facadeModule: { isUserDefinedEntryPoint: true }, getPreliminaryFileName: () => 'entry4.js' }
]

// Process chunks for name reservation
// Expected: All 4 entry chunks should have getPreliminaryFileName() called
// Actual: Only 2 chunks are processed (every other one is skipped)
```

### Expected behavior

All user-defined entry point chunks should have their preliminary file names reserved in the bundle. Currently, it appears that only every other entry chunk is being processed correctly.

### Additional context

This seems to affect builds with multiple entry points where the chunk name reservation is critical for avoiding conflicts. The issue manifests as some entry chunks not getting their names properly reserved while others do.

---
Repository: /testbed
