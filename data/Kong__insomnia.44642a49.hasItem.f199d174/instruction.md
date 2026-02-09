# Bug Report

### Describe the bug

The `hasItem()` method in the plugin store is returning incorrect boolean values. When checking if a key exists in the plugin data store, it returns `true` when the item does NOT exist (doc is null) and returns a value based on `undefined` check when the item DOES exist.

### Reproduction

```js
// Assuming a plugin context with store access
const { store } = context;

// Check for a key that doesn't exist in the store
const exists = await store.hasItem('nonexistent-key');
console.log(exists); // Expected: false, Actual: true

// Set an item
await store.setItem('my-key', 'my-value');

// Check for the key that now exists
const existsNow = await store.hasItem('my-key');
console.log(existsNow); // Expected: true, Actual: depends on whether doc is undefined
```

### Expected behavior

`hasItem()` should return `true` when a key exists in the plugin data store and `false` when it doesn't exist. Currently the logic appears to be inverted.

### System Info

- Insomnia version: latest
- Plugin API being used

This is making it impossible to reliably check for the existence of plugin data before attempting to read or write values.

---
Repository: /testbed
