# Bug Report

### Describe the bug

The plugin cache eviction logic appears to be broken. When using `experimentalCacheExpiry`, cache entries that should be deleted are being kept, and cache entries that should be kept are being deleted. Additionally, entire plugin caches are being removed when they shouldn't be.

### Reproduction

```js
// Set up a graph with experimentalCacheExpiry
const graph = new Graph({
  experimentalCacheExpiry: 10
});

// Add some cache entries with different ages
graph.pluginCache['myPlugin'] = {
  'key1': [5, 'data1'],  // Should be kept (5 < 10)
  'key2': [15, 'data2']  // Should be deleted (15 >= 10)
};

// Call getCache() to trigger eviction
graph.getCache();

// Expected: key1 should exist, key2 should be deleted
// Actual: opposite behavior occurs
```

### Expected behavior

- Cache entries with age >= `experimentalCacheExpiry` should be evicted
- Cache entries with age < `experimentalCacheExpiry` should be retained  
- Plugin cache should only be deleted when ALL its entries are evicted
- If at least one entry remains, the plugin cache itself should be kept

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be a logic error in the cache eviction code. The behavior is completely inverted from what's expected.

---
Repository: /testbed
