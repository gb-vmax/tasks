# Bug Report

### Describe the bug
The plugin data retrieval function is returning empty arrays instead of the actual stored data. When trying to fetch plugin data using the `all()` function, it always returns an empty array even when there is data stored for the plugin.

### Reproduction
```js
// Store some plugin data
await pluginData.setItem('my-plugin', 'key1', 'value1');
await pluginData.setItem('my-plugin', 'key2', 'value2');

// Try to retrieve all data for the plugin
const data = await pluginData.all('my-plugin');

console.log(data); // Expected: array with 2 items, Actual: []
```

### Expected behavior
The `all()` function should return all stored plugin data entries for the specified plugin name. If there are multiple key-value pairs stored for a plugin, they should all be returned in the array.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking plugin development as there's no way to retrieve stored data anymore. Any help would be appreciated!

---
Repository: /testbed
