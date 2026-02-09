# Bug Report

### Describe the bug

After a recent update, the plugin store's `hasItem()` method is not working correctly when checking for items that were just added via `setItem()`. The method returns `false` even though the item exists in the store.

### Reproduction

```js
// Set an item in the plugin store
await store.setItem('myKey', 'myValue');

// Immediately check if the item exists
const exists = await store.hasItem('myKey');
console.log(exists); // Expected: true, Actual: false
```

The issue seems to happen when:
1. You call `setItem()` to add/update a value
2. Immediately after, call `hasItem()` with the same key
3. `hasItem()` returns `false` even though the item was just stored

This is causing problems in my plugin where I need to verify that data was successfully saved before proceeding with other operations.

### Expected behavior

`hasItem()` should return `true` immediately after `setItem()` is called with the same key, reflecting the current state of the store.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
