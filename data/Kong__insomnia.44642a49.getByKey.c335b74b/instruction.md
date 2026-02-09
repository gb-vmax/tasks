# Bug Report

### Describe the bug

The `getByKey` function in the plugin-data model is not filtering by the `key` parameter. When trying to retrieve plugin data for a specific key, it returns all data for the plugin instead of just the data associated with that key.

### Reproduction

```js
// Store some plugin data with different keys
await pluginData.set('my-plugin', 'config', { setting: 'value1' });
await pluginData.set('my-plugin', 'cache', { data: 'value2' });

// Try to get data for a specific key
const result = await pluginData.getByKey('my-plugin', 'config');

// Expected: Only the 'config' data
// Actual: Returns data for the entire plugin (both 'config' and 'cache')
```

### Expected behavior

`getByKey('my-plugin', 'config')` should return only the plugin data associated with the 'config' key, not all data for 'my-plugin'.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
