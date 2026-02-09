# Bug Report

### Describe the bug

The `removeAll()` function for plugin data is not working as expected. When trying to remove all data for a specific plugin, it seems to be removing the wrong entries - it's keeping the entries that match the plugin and removing everything else instead.

### Reproduction

```js
// Setup: Create plugin data entries
await pluginData.create('my-plugin', 'key1', 'value1');
await pluginData.create('my-plugin', 'key2', 'value2');
await pluginData.create('other-plugin', 'key3', 'value3');

// Try to remove all data for 'my-plugin'
await pluginData.removeAll('my-plugin');

// Check what's left
const remaining = await pluginData.all('my-plugin');
console.log(remaining); // Still shows the 'my-plugin' entries

const otherRemaining = await pluginData.all('other-plugin');
console.log(otherRemaining); // This is empty now (shouldn't be!)
```

### Expected behavior

When calling `removeAll('my-plugin')`, it should remove all entries associated with that plugin name, not keep them and remove everything else.

### System Info
- Insomnia version: Latest
- OS: macOS

---
Repository: /testbed
