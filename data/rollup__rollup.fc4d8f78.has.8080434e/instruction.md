# Bug Report

### Describe the bug

The plugin cache's `has()` method is returning incorrect values. When checking if a cached plugin exists, it always returns `false` even when the plugin is actually present in the cache.

### Reproduction

```js
const cache = createPluginCache({});

// Add a plugin to the cache
cache.set('my-plugin', { some: 'data' });

// This should return true but returns false
const exists = cache.has('my-plugin');
console.log(exists); // Expected: true, Actual: false

// But we can still retrieve the value
const value = cache.get('my-plugin');
console.log(value); // { some: 'data' } - the plugin is actually there!
```

### Expected behavior

The `has()` method should return `true` when a plugin exists in the cache and `false` when it doesn't. Currently it always returns `false` regardless of whether the plugin is cached or not.

This is causing issues with plugin loading logic that relies on checking cache existence before attempting to retrieve values.

---
Repository: /testbed
