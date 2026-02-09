# Bug Report

### Describe the bug

I'm experiencing an issue with error handling in the watch system. When an error occurs during the build process, the cache modules are not being properly filtered/cleaned up. Instead of removing the problematic module from the cache, it seems like the wrong modules are being kept or removed.

### Reproduction

```js
// Set up a watch task with some cached modules
const task = new Task({
  cache: {
    modules: [
      { id: 'module-a' },
      { id: 'module-b' },
      { id: 'module-c' }
    ]
  }
});

// When an error occurs with module-b
// Expected: module-b should be removed from cache
// Actual: module-b is kept, other modules are removed
```

This appears to happen when the watcher encounters an error and tries to update the module cache. The module that caused the error remains in the cache while other modules get filtered out incorrectly.

### Expected behavior

When an error occurs with a specific module ID, that module should be removed from the cache, not the other way around. The cache should only retain modules that are still valid.

### Additional context

This is causing issues in watch mode where subsequent builds fail because the cache contains stale/errored modules that should have been cleared.

---
Repository: /testbed
