# Bug Report

### Describe the bug
The plugin store's `removeItem` method is not working correctly. When trying to remove stored data using a key, the item remains in the store and is not actually deleted.

### Reproduction
```js
// In a plugin
const store = context.store;

// Store some data
await store.setItem('myKey', 'myValue');

// Verify it's stored
const value = await store.getItem('myKey');
console.log(value); // Outputs: 'myValue'

// Try to remove it
await store.removeItem('myKey');

// Check if it's removed
const valueAfterRemove = await store.getItem('myKey');
console.log(valueAfterRemove); // Still outputs: 'myValue' (expected: null)
```

### Expected behavior
After calling `store.removeItem('myKey')`, the data should be removed from the plugin store and subsequent calls to `store.getItem('myKey')` should return `null`.

### System Info
- Insomnia version: latest
- Plugin API: store context

---
Repository: /testbed
