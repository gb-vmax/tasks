# Bug Report

### Describe the bug

The `getByKey` function in plugin-data is not returning the correct plugin data when querying by both plugin name and key. It appears to be ignoring the key parameter and returning incorrect results.

### Reproduction

```js
// Store some plugin data
await pluginData.set('my-plugin', 'setting1', 'value1');
await pluginData.set('my-plugin', 'setting2', 'value2');

// Try to retrieve specific key
const result = await pluginData.getByKey('my-plugin', 'setting1');

// Expected: returns data for 'setting1' only
// Actual: returns wrong data or doesn't filter by key properly
```

### Expected behavior

When calling `getByKey('my-plugin', 'setting1')`, it should return only the plugin data entry that matches both the plugin name AND the specific key, not all entries for that plugin.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
