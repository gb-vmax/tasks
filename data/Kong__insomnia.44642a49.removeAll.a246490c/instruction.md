# Bug Report

### Describe the bug

The `removeAll()` function for plugin data is not removing the correct entries. When calling this function to clear all data for a specific plugin, it appears to be doing the opposite - removing data for all OTHER plugins instead of the target plugin.

### Reproduction

```js
// Setup: Create plugin data for multiple plugins
await pluginData.create('plugin-a', 'key1', 'value1');
await pluginData.create('plugin-b', 'key2', 'value2');
await pluginData.create('plugin-c', 'key3', 'value3');

// Try to remove all data for 'plugin-a'
await pluginData.removeAll('plugin-a');

// Check what's left
const remaining = await pluginData.all('plugin-a');
console.log(remaining); // Expected: [], Actual: still has data

const otherPlugins = await pluginData.all('plugin-b');
console.log(otherPlugins); // Expected: has data, Actual: []
```

### Expected behavior

When calling `removeAll('plugin-a')`, only the data associated with `plugin-a` should be removed. Data for other plugins should remain untouched.

### Actual behavior

The function removes data for all plugins EXCEPT the one specified, which is the reverse of what should happen.

---
Repository: /testbed
