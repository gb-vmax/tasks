# Bug Report

### Describe the bug

The plugin store's `clear()` method is not working correctly - it's clearing data for a different plugin instead of the current one. When I call `store.clear()` from my plugin, it doesn't actually clear my plugin's data.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  async context => {
    const { store } = context;
    
    // Store some data
    await store.setItem('key1', 'value1');
    await store.setItem('key2', 'value2');
    
    // Try to clear all data
    await store.clear();
    
    // Data is still there!
    const value = await store.getItem('key1');
    console.log(value); // Still returns 'value1' instead of null
  }
];
```

### Expected behavior

After calling `store.clear()`, all data stored by the plugin should be removed. Subsequent calls to `getItem()` should return `null` for previously stored keys.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like it might be related to how the plugin is identified internally. Other store methods like `setItem`, `getItem`, and `removeItem` work fine - it's only `clear()` that has this issue.

---
Repository: /testbed
