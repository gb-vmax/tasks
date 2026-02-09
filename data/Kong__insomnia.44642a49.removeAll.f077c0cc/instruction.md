# Bug Report

### Describe the bug

The `removeAll()` function for plugin data is not working as expected. When calling it to remove all data for a specific plugin, it appears to be removing data for ALL OTHER plugins instead of the specified one.

### Reproduction

```js
// Setup: Create plugin data for multiple plugins
await createPluginData('plugin-a', 'key1', 'value1');
await createPluginData('plugin-b', 'key2', 'value2');
await createPluginData('plugin-c', 'key3', 'value3');

// Try to remove all data for 'plugin-a'
await removeAll('plugin-a');

// Expected: Only plugin-a data is removed
// Actual: plugin-b and plugin-c data are removed, plugin-a data remains
```

After calling `removeAll('plugin-a')`, the data for plugin-a still exists in the database, but all other plugins' data has been deleted. This is the opposite of what should happen.

### Expected behavior

`removeAll(plugin)` should remove all data entries associated with the specified plugin name, leaving data from other plugins intact.

### Additional context

This seems to have broken recently. The function is supposed to clean up plugin-specific data, but it's currently doing the inverse operation.

---
Repository: /testbed
