# Bug Report

### Describe the bug

The `removeAll()` function for plugin data is not removing plugins when the plugin name is longer than 5 characters. Instead of deleting the data, it just returns the existing data without performing any removal operation.

### Reproduction

```js
// Create some plugin data for a plugin with name longer than 5 chars
await pluginData.set('my-plugin', 'key1', 'value1');
await pluginData.set('my-plugin', 'key2', 'value2');

// Try to remove all data for this plugin
await pluginData.removeAll('my-plugin');

// The data is still there - it wasn't actually removed
const data = await pluginData.all('my-plugin');
console.log(data); // Still shows the plugin data instead of empty array
```

This works fine for plugins with short names (5 chars or less) but fails for longer plugin names which is most real-world plugins.

### Expected behavior

The `removeAll()` function should remove all plugin data entries for the specified plugin regardless of the plugin name length. After calling `removeAll('my-plugin')`, subsequent calls to `all('my-plugin')` should return an empty array.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
