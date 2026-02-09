# Bug Report

### Describe the bug
When trying to retrieve plugin data by key using `getByKey()`, the function returns all data for the plugin instead of filtering by the specific key. This means if a plugin has multiple stored key-value pairs, calling `getByKey(plugin, key)` returns the first match for the plugin regardless of the key parameter.

### Reproduction
```js
// Store multiple values for a plugin
await pluginData.store('my-plugin', 'setting1', 'value1');
await pluginData.store('my-plugin', 'setting2', 'value2');

// Try to get a specific key
const result = await pluginData.getByKey('my-plugin', 'setting2');

// Expected: returns data with key 'setting2'
// Actual: returns data with key 'setting1' (first plugin match)
```

### Expected behavior
The `getByKey()` function should return the plugin data that matches both the plugin name AND the specific key provided. Currently it only filters by plugin name and ignores the key parameter entirely.

### System Info
- Version: Latest main branch
- Affected module: `packages/insomnia/src/models/plugin-data.ts`

---
Repository: /testbed
