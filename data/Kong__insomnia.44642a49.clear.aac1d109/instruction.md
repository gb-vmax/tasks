# Bug Report

### Describe the bug

After updating the plugin store implementation, calling `store.clear()` is creating unexpected backup entries in the store instead of just clearing the data. The store now contains `__backup_*` keys that persist even after clearing, which causes issues when trying to retrieve all plugin data.

### Reproduction

```js
// Initialize plugin store
const { store } = initPluginStore(myPlugin);

// Add some data
await store.setItem('key1', 'value1');
await store.setItem('key2', 'value2');

// Clear the store
await store.clear();

// Check what's in the store
const allData = await store.all();
console.log(allData);
// Expected: []
// Actual: Contains __backup_* entries with timestamp and stored data
```

### Expected behavior

When calling `store.clear()`, the store should be completely empty. It should not create any backup entries or leave any residual data behind. The `all()` method should return an empty array after clearing.

### Additional context

This seems to have started happening recently. The backup functionality might be useful for debugging, but it shouldn't be automatically triggered on every clear operation as it pollutes the store and breaks existing plugin behavior that expects a clean state after clearing.

---
Repository: /testbed
