# Bug Report

### Describe the bug

After a recent update, plugin data initialization is failing when trying to access the `key` property. It seems like the `key` field is no longer being initialized in the plugin data model, causing undefined behavior when plugins try to read or write data.

### Reproduction

```js
const pluginData = init();

// This now returns undefined instead of an empty string
console.log(pluginData.key);

// Trying to use the key property causes issues
if (pluginData.key === '') {
  // This condition no longer works as expected
}
```

### Expected behavior

The `init()` function should return a plugin data object with all required fields initialized, including the `key` property as an empty string. Plugins that depend on this field being present are now breaking.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
