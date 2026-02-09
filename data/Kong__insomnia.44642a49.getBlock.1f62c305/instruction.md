# Bug Report

### Describe the bug

I'm experiencing an issue with the diff/sync functionality where the delta calculation seems to be producing incorrect results. When comparing two strings, the generated operations don't correctly identify the differences between the source and target.

### Reproduction

```js
const source = "Hello World";
const target = "Hello Universe";
const blockSize = 4;

const operations = diff(source, target, blockSize);
// The operations generated don't correctly represent the actual differences
// Expected to see proper block-level changes, but getting incorrect hash matches
```

### Expected behavior

The diff function should correctly identify which blocks have changed between the source and target strings. Currently, it appears to be matching blocks incorrectly, likely causing sync issues when trying to apply the delta operations.

### Additional context

This seems to affect any string comparison where blocks need to be analyzed. The hash calculation for blocks doesn't seem to be working as intended - it's matching blocks that shouldn't match, which could lead to data corruption during sync operations.

---
Repository: /testbed
