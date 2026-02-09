# Bug Report

### Describe the bug

The plugin store's `removeItem()` method is removing all items EXCEPT the one specified by the key parameter, instead of removing the item with that key. This is causing data to be incorrectly deleted from the plugin storage.

### Reproduction

```js
// Initialize plugin store
const store = plugin.store;

// Add some items
await store.setItem('key1', 'value1');
await store.setItem('key2', 'value2');
await store.setItem('key3', 'value3');

// Try to remove key2
await store.removeItem('key2');

// Check what's left
const remaining1 = await store.getItem('key1'); // Returns null (incorrectly deleted)
const remaining2 = await store.getItem('key2'); // Returns 'value2' (should be null!)
const remaining3 = await store.getItem('key3'); // Returns null (incorrectly deleted)
```

### Expected behavior

When calling `store.removeItem('key2')`, only the item with key 'key2' should be removed. All other items should remain in the store. Instead, the opposite is happening - all items EXCEPT 'key2' are being removed.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
