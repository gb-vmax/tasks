# Bug Report

### Describe the bug

I'm experiencing an issue with the sync delta diff functionality where blocks are being incorrectly sliced. When processing text blocks, the last character of each block is being omitted, which causes data loss during synchronization.

### Reproduction

```js
const source = "Hello World";
const target = "Hello World!";
const blockSize = 5;

const result = diff(source, target, blockSize);
// The blocks don't contain the expected characters
// Block 1: "Hell" instead of "Hello"
// Block 2: " Wor" instead of " Worl"
```

When I try to sync content using the diff function, I notice that:
1. Each block is missing its last character
2. This leads to incorrect diff operations being generated
3. The synchronized content ends up corrupted or incomplete

### Expected behavior

The diff function should correctly slice blocks to include all characters within the specified block size. For a blockSize of 5, the first block should contain 5 characters, not 4.

### Additional context

This seems to have started happening recently. The block slicing logic appears to be off by one, causing each block to be one character shorter than intended. This is particularly problematic when syncing larger documents as the accumulated missing characters result in significant data corruption.

---
Repository: /testbed
