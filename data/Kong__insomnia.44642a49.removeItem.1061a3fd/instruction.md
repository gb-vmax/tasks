# Bug Report

### Describe the bug

The plugin store's `removeItem` method doesn't actually remove items anymore. When I call `store.removeItem(key)` to delete a stored value, the item remains in the store and can still be retrieved with `getItem`.

### Reproduction

```js
const store = context.store;

// Set a value
await store.setItem('myKey', 'myValue');

// Try to remove it
await store.removeItem('myKey');

// The value is still there!
const value = await store.getItem('myKey');
console.log(value); // Still returns 'myValue' instead of null
```

### Expected behavior

After calling `removeItem`, the key should be deleted from the plugin store and subsequent calls to `getItem` with that key should return `null`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
