# Bug Report

### Describe the bug
The `getByKey()` function in plugin-data is returning incorrect results when querying for plugin data. Instead of finding the specific plugin data entry that matches both the plugin name AND the key, it's returning data that matches EITHER the plugin name OR the key.

This means if you try to get data for a specific plugin with a specific key, you might get back data from a completely different plugin that happens to use the same key name.

### Reproduction
```js
// Assume we have two plugins with data stored:
// Plugin A: { plugin: 'pluginA', key: 'config', data: { value: 'A' } }
// Plugin B: { plugin: 'pluginB', key: 'config', data: { value: 'B' } }

// Try to get config for pluginA
const result = await getByKey('pluginA', 'config');

// Expected: Gets data for pluginA with key 'config'
// Actual: Might return data for pluginB if the first query fails
```

### Expected behavior
`getByKey(plugin, key)` should only return plugin data that matches both the plugin name AND the key. If no exact match exists, it should return null/undefined, not fall back to data from other plugins.

### System Info
- Version: Latest from main branch

---
Repository: /testbed
