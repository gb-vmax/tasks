# Bug Report

### Describe the bug

The plugin cache is not working correctly - it always reports that cached items don't exist even when they do. This breaks caching functionality and causes plugins to be unnecessarily reprocessed.

### Reproduction

```js
const cache = createPluginCache({});

// Add an item to cache
cache.set('my-plugin', { data: 'test' });

// Check if item exists
console.log(cache.has('my-plugin')); // Expected: true, Actual: false

// The item is actually in cache and can be retrieved
console.log(cache.get('my-plugin')); // Returns: { data: 'test' }
```

### Expected behavior

`cache.has()` should return `true` when an item exists in the cache. Currently it always returns `false` even for items that were just added.

### Additional context

This seems to have broken recently. The cache is storing items correctly (as evidenced by `get()` working), but the `has()` method is not detecting them properly.

---
Repository: /testbed
