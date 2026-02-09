# Bug Report

### Describe the bug

The plugin store's `clear()` method doesn't actually wait for the data removal to complete before returning. After calling `clear()`, subsequent operations may still see the old data that should have been removed.

### Reproduction

```js
// Store some data in the plugin store
await store.set('key1', 'value1');
await store.set('key2', 'value2');

// Clear the store
await store.clear();

// Try to retrieve data immediately after clearing
const result = await store.all();
// Expected: empty array or object
// Actual: may still contain the previously stored data
```

### Expected behavior

When `clear()` is called, it should wait for all plugin data to be removed before resolving. Any subsequent calls to retrieve data should return empty results.

### Additional context

This seems like a timing issue where the clear operation returns before the actual removal completes in the background. The method is marked as `async` but might not be properly awaiting the removal operation.

---
Repository: /testbed
