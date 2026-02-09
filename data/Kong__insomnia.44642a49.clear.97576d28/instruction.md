# Bug Report

### Describe the bug
The plugin store's `clear()` method is not removing all stored data for a plugin. After calling `clear()`, previously stored key-value pairs are still accessible when using `getItem()` or `all()`.

### Reproduction
```js
// Store some data for a plugin
await store.setItem('key1', 'value1');
await store.setItem('key2', 'value2');

// Verify data exists
const allBefore = await store.all();
console.log(allBefore); // Shows key1 and key2

// Clear all data
await store.clear();

// Data should be gone but still exists
const allAfter = await store.all();
console.log(allAfter); // Still shows key1 and key2 (unexpected!)

const value = await store.getItem('key1');
console.log(value); // Still returns 'value1' instead of undefined
```

### Expected behavior
After calling `store.clear()`, all data associated with the plugin should be removed. Subsequent calls to `getItem()` should return `undefined` and `all()` should return an empty array.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
