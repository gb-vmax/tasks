# Bug Report

### Describe the bug
After a recent update, the sync delta diff algorithm seems to be producing incorrect results when comparing text blocks. I'm seeing cases where identical content is being marked as changed, or changes are not being detected properly.

### Reproduction
```js
const text1 = "Hello World";
const text2 = "Hello World";

// Running diff on identical strings
const delta = diff(text1, text2);

// Expected: no changes
// Actual: shows modifications even though content is identical
```

Another case I noticed:
```js
const original = "ABCDEFGHIJ";
const modified = "ABCDEFGHIJ";

// With small block sizes, the diff is not working as expected
const result = diff(original, modified, { blockSize: 32 });
// Returns unexpected deltas
```

### Expected behavior
When comparing identical strings, the diff should return no changes. The algorithm should correctly identify matching blocks regardless of the block size configuration.

### Additional context
This appears to be related to how blocks are being tracked and merged during the diff process. The issue is more noticeable with smaller block sizes (64 or less), but can also occur with larger blocks near the end of strings.

---
Repository: /testbed
