# Bug Report

### Describe the bug

I'm encountering an issue with the sync delta/diff functionality where block operations are producing incorrect results. When syncing content, the block length calculation seems to be off by one, which causes downstream synchronization errors.

### Reproduction

```js
// When diffing two strings with a specific block size
const source = "hello world";
const target = "hello there";
const blockSize = 5;

const operations = diff(source, target, blockSize);

// The block lengths in the operations are incorrect
// Expected block length: 5 (for "hello")
// Actual block length: 6 (one more than expected)
```

This affects sync operations where precise block boundaries are critical for correctly applying changes.

### Expected behavior

Block length should match the actual slice length, not be incremented. When a block is extracted from position `start` with `blockSize`, the resulting block should have length equal to the slice length (which is `min(blockSize, remaining_length)`).

### Additional context

This appears to affect the hash calculation and block matching logic during sync operations. The boundary check at `start >= value.length` also seems too strict - it prevents getting a block at the exact end position when `start == value.length`.

---
Repository: /testbed
