# Bug Report

### Describe the bug

I'm experiencing an issue where the first plugin in the plugin chain is being skipped during hook execution. When using `hookFirstSync`, only plugins starting from the second position are being processed, which means the first registered plugin never gets its hooks called.

### Reproduction

```js
// Register multiple plugins with the same hook
const plugins = [
  {
    name: 'plugin-1',
    resolveId(id) {
      console.log('plugin-1 called');
      return 'resolved-by-plugin-1';
    }
  },
  {
    name: 'plugin-2',
    resolveId(id) {
      console.log('plugin-2 called');
      return null;
    }
  }
];

// Expected: plugin-1 should be called first and return its result
// Actual: plugin-1 is skipped, only plugin-2 gets called
```

### Expected behavior

The `hookFirstSync` method should iterate through all plugins starting from index 0, and the first plugin that returns a non-null result should have its value returned. Currently, the first plugin in the array is being completely ignored.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
