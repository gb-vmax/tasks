# Bug Report

### Describe the bug

The `getByKey` function for plugin data is returning incorrect results. When trying to retrieve plugin data by key, the function appears to be swapping the parameters, causing lookups to fail or return wrong data.

### Reproduction

```js
// Store some plugin data
await pluginData.set('my-plugin', 'config-key', { value: 'test' });

// Try to retrieve it
const data = await pluginData.getByKey('my-plugin', 'config-key');

// Returns null or wrong data instead of the stored value
console.log(data); // Expected: { value: 'test' }, Actual: null
```

### Expected behavior

`getByKey('my-plugin', 'config-key')` should return the plugin data that was stored with that plugin name and key combination.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
