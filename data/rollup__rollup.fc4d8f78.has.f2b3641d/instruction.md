# Bug Report

### Describe the bug

The `PluginCache.has()` method is not working correctly - it always returns `false` even when the cache contains the requested item. This breaks cache lookups and causes plugins to be unnecessarily reprocessed.

### Reproduction

```js
const cache = createPluginCache({});

// Add an item to the cache
cache.set('my-plugin', { some: 'data' });

// Check if the item exists
console.log(cache.has('my-plugin')); // Expected: true, Actual: false
```

### Expected behavior

When an item exists in the cache, `has()` should return `true`. Currently it always returns `false` regardless of whether the item is present or not.

### Additional context

This seems to have broken recently. The cache is being populated correctly (verified by checking `get()` which returns the cached values), but `has()` always returns `false` which defeats the purpose of having a cache check.

---
Repository: /testbed
