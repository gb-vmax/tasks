# Bug Report

### Describe the bug

The `removeAll` function for plugin data isn't actually removing data anymore. When I try to clear all data for a specific plugin, the data remains in the database instead of being deleted.

### Reproduction

```js
// Store some plugin data
await pluginData.set('my-plugin', 'key1', 'value1');
await pluginData.set('my-plugin', 'key2', 'value2');

// Try to remove all data for the plugin
await pluginData.removeAll('my-plugin');

// Check if data still exists
const remaining = await pluginData.all('my-plugin');
console.log(remaining); // Expected: [], Actual: [{ key: 'key1', value: 'value1' }, { key: 'key2', value: 'value2' }]
```

### Expected behavior

All plugin data associated with the specified plugin should be removed from the database. The `removeAll` function should delete all records matching the plugin name.

### Additional context

This seems to have broken recently. The function appears to be querying for data instead of removing it. I'm using this to clean up plugin data when uninstalling plugins, and now the data persists even after uninstall.

---
Repository: /testbed
