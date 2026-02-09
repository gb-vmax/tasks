# Bug Report

### Describe the bug

I'm experiencing a memory leak issue with the sync/delta diff functionality. After performing multiple diff operations, memory usage keeps growing and doesn't get released even after the operations complete.

### Reproduction

```js
// Perform multiple diff operations in sequence
for (let i = 0; i < 1000; i++) {
  const source = "some large text content...";
  const target = "modified large text content...";
  diff(source, target, 64);
}

// Memory usage continues to grow and isn't released
```

The problem seems to get worse with larger strings and more iterations. After running several hundred diff operations, I'm seeing significant memory consumption that doesn't get garbage collected.

### Expected behavior

Memory should be properly managed and released after diff operations complete. There shouldn't be unbounded memory growth when performing multiple diff operations.

### System Info
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
