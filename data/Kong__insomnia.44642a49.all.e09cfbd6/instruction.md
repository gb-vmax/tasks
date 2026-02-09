# Bug Report

### Describe the bug

The `all()` function in the plugin-data model is not returning the correct data. When trying to retrieve all plugin data for a specific plugin, the function returns data from all plugins instead of filtering by the requested plugin name.

### Reproduction

```js
// Store some data for different plugins
await pluginData.set('plugin-a', 'key1', 'value1');
await pluginData.set('plugin-b', 'key2', 'value2');

// Try to get all data for plugin-a only
const dataForPluginA = await pluginData.all('plugin-a');

// Expected: Only data for plugin-a
// Actual: Returns data for all plugins (plugin-a and plugin-b)
console.log(dataForPluginA);
```

### Expected behavior

The `all()` function should return only the plugin data entries that belong to the specified plugin. When calling `pluginData.all('plugin-a')`, it should only return data associated with 'plugin-a', not data from other plugins.

### Additional context

This is causing issues when trying to manage plugin-specific data, as there's no way to retrieve data for a single plugin without getting everything from the database. This could lead to data leakage between plugins or incorrect data being used.

---
Repository: /testbed
