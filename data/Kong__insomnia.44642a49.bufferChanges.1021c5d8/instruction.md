# Bug Report

### Describe the bug

After updating to the latest version, I'm experiencing issues with database change buffering. When multiple rapid database changes are made, the buffer doesn't flush properly and some changes seem to get lost or not persisted correctly.

### Reproduction

```js
// Make rapid successive database changes
for (let i = 0; i < 100; i++) {
  await database.bufferChanges(1000);
  // ... make some database changes
}

// Expected: All changes should be flushed after the timeout
// Actual: Some changes don't get persisted
```

The issue seems to happen when:
1. Multiple `bufferChanges()` calls are made in quick succession
2. Each call creates a new buffer with its own timeout
3. Changes from earlier buffers don't always get flushed correctly

### Expected behavior

All buffered changes should be properly flushed after the specified timeout period, regardless of how many times `bufferChanges()` is called. The buffer system should handle multiple concurrent buffers without losing data.

### Additional context

This worked fine in the previous version. The problem started appearing after the recent update. It's particularly noticeable when making bulk database operations or when the application is under heavy load with many database writes happening simultaneously.

---
Repository: /testbed
