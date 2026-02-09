# Bug Report

### Describe the bug

I'm experiencing memory issues when using the sync diff functionality with large files or when performing multiple diff operations in succession. The application's memory usage keeps growing and doesn't seem to be released even after the diff operations complete.

### Reproduction

```js
// Perform multiple diff operations on moderately sized strings
const source = 'a'.repeat(10000);
const target = 'b'.repeat(10000);

for (let i = 0; i < 100; i++) {
  diff(source, target, 512);
}

// Memory usage keeps increasing with each iteration
```

The memory footprint grows significantly when:
1. Processing large source strings
2. Running multiple diff operations sequentially
3. Using the same source string repeatedly

### Expected behavior

Memory should be released after diff operations complete. The memory usage should remain relatively stable when performing multiple diff operations, especially when reusing the same source strings.

### System Info
- Node version: 18.x
- OS: macOS

This seems to have started after a recent update. The diff functionality still works correctly, but the memory consumption is concerning for long-running processes.

---
Repository: /testbed
