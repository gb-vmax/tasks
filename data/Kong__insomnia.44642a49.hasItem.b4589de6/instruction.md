# Bug Report

### Describe the bug

The `hasItem()` method in the plugin store context is not properly checking if items with TTL (time-to-live) have expired. When a stored item has expired based on its TTL metadata, `hasItem()` still returns `true` instead of `false`, leading to stale data being considered as valid.

### Reproduction

```js
// Store an item with TTL metadata
await store.setItem('test-key', JSON.stringify({
  __ttl_metadata__: {
    expiresAt: Date.now() - 1000 // Already expired
  },
  value: 'some-data'
}));

// Check if item exists - should return false but returns true
const exists = await store.hasItem('test-key');
console.log(exists); // Expected: false, Actual: true
```

### Expected behavior

When an item with TTL metadata has expired (current time > expiresAt), `hasItem()` should:
1. Return `false` to indicate the item doesn't exist
2. Remove the expired item from storage

### System Info
- Insomnia version: latest
- Platform: All platforms

This causes issues where plugins continue to use expired cached data thinking it's still valid.

---
Repository: /testbed
