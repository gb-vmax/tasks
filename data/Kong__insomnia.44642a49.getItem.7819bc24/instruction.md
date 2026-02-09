# Bug Report

### Describe the bug

After a recent update, the plugin store's `setItem` and `getItem` methods are not working together correctly. When I set a value using `setItem`, subsequent calls to `getItem` for the same key return stale data instead of the updated value.

### Reproduction

```js
const store = context.store;

// Set an initial value
await store.setItem('myKey', 'initialValue');
console.log(await store.getItem('myKey')); // Returns 'initialValue' ✓

// Update the value
await store.setItem('myKey', 'updatedValue');
console.log(await store.getItem('myKey')); // Returns 'initialValue' ✗ (should return 'updatedValue')
```

### Expected behavior

After calling `setItem` with a new value, `getItem` should immediately return the updated value, not the old cached value.

### Additional context

This seems to have started happening recently. The store appears to be caching values but not invalidating the cache when items are updated. This is causing issues in my plugin where I need to store and retrieve configuration values dynamically.

---
Repository: /testbed
