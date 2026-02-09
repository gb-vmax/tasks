# Bug Report

### Describe the bug

I'm experiencing an issue with the sync delta diff functionality where duplicate blocks in the input string are not being properly tracked. When the same content block appears multiple times in a string, only the last occurrence is preserved in the block map, causing previous occurrences to be lost.

### Reproduction

```js
// When processing a string with repeating patterns
const input = "hello world hello world";
const blockMap = getBlockMap(input, 5);

// Expected: blocks with the same hash should all be tracked
// Actual: only the last block with each hash is kept
```

This seems to affect synchronization when dealing with files that have repeated content sections. The diff algorithm is missing duplicate blocks, which could lead to incorrect sync operations.

### Expected behavior

All blocks with the same hash should be stored in the block map array, not just the last one. This is important for accurately tracking all occurrences of repeated content during the diff process.

### System Info
- Insomnia version: latest
- Affected module: sync/delta/diff.ts

---
Repository: /testbed
