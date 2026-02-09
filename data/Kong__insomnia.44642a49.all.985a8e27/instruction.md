# Bug Report

### Describe the bug

The `all()` function in the plugin-data model is returning incorrect results. When I try to retrieve all data for a specific plugin, it seems to be returning data from other plugins instead, or not returning the expected data at all.

### Reproduction

```js
// Store some data for a plugin
await pluginData.set('my-plugin', 'key1', 'value1');
await pluginData.set('my-plugin', 'key2', 'value2');
await pluginData.set('other-plugin', 'key3', 'value3');

// Try to get all data for 'my-plugin'
const data = await pluginData.all('my-plugin');

// Expected: Should return all entries for 'my-plugin' (key1 and key2)
// Actual: Returns entries from other plugins or empty/limited results
console.log(data); // Not showing the expected plugin data
```

### Expected behavior

The `all()` function should return all stored data entries for the specified plugin name. If I have multiple key-value pairs stored for a plugin, calling `all('my-plugin')` should return all of them.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking plugin functionality that relies on retrieving all stored data. Any help would be appreciated!

---
Repository: /testbed
