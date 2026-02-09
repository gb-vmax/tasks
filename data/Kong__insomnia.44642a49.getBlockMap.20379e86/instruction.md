# Bug Report

### Describe the bug

I'm experiencing performance issues after a recent update. When working with large strings in the sync functionality, the application becomes unresponsive and eventually times out. This seems to be related to the diff calculation process.

### Reproduction

```js
const largeString = 'a'.repeat(50000);
const modifiedString = largeString.slice(0, 25000) + 'b' + largeString.slice(25001);

// This operation hangs/takes extremely long
const delta = diff(largeString, modifiedString);
```

The issue appears when:
1. Working with strings larger than ~10KB
2. Using smaller block sizes (e.g., blockSize <= 16)
3. The diff calculation seems to generate an excessive number of blocks

### Expected behavior

The diff operation should complete in a reasonable time even for large strings. Previous versions handled this without issues.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our ability to sync large request bodies. Any help would be appreciated!

---
Repository: /testbed
