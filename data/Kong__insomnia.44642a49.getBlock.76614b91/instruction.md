# Bug Report

### Describe the bug

I'm experiencing memory issues when syncing large files. The application becomes unresponsive and eventually crashes with an out-of-memory error during diff operations. This seems to happen consistently when processing files larger than a few MB.

### Reproduction

```js
// Syncing a large document repeatedly
const source = "a".repeat(100000);
const target = "b".repeat(100000);

// Perform multiple diff operations
for (let i = 0; i < 1000; i++) {
  diff(source, target, 1024);
}

// Memory usage grows unbounded and doesn't get released
```

### Expected behavior

Memory should be released after each diff operation completes. The application should handle multiple sync operations without accumulating memory usage.

### System Info
- Node version: 18.x
- OS: macOS 14

This wasn't happening in previous versions, so it might be related to recent changes in the sync/delta module.

---
Repository: /testbed
