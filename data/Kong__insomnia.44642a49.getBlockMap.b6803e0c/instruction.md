# Bug Report

### Describe the bug

I'm experiencing an issue with the sync delta diff algorithm where text blocks are being incorrectly indexed when building the block map. When processing strings with repeating patterns, the block positions seem to get misaligned, causing the diff calculation to produce incorrect results.

### Reproduction

```js
// When processing a string with repeating blocks
const text = "ABCABCABC";
const blockSize = 3;

// The block map generation appears to skip over blocks incorrectly
// causing positions to be off when the same hash appears multiple times
```

This seems to happen specifically when:
1. A block hash already exists in the map
2. The same pattern repeats in the text
3. Block boundaries overlap or are adjacent

### Expected behavior

The block map should correctly track all block positions regardless of whether the hash already exists in the map. Each block should advance the position counter by the appropriate amount to ensure all blocks are properly indexed.

### System Info
- Version: Latest from main branch
- Affects: Sync delta diff functionality

---
Repository: /testbed
