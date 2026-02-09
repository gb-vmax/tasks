# Bug Report

### Describe the bug

After a recent update, plugin data keys are being modified in unexpected ways. Keys that contain consecutive dots or leading/trailing dots are being altered, which breaks existing plugin configurations that rely on specific key formats.

### Reproduction

```js
// Plugin data with dots in keys
const pluginData = {
  key: 'my.plugin..config',
  value: 'some value'
}

// After migration, the key is changed to 'my.plugin.config'
// This breaks lookups for the original key
```

Another example:
```js
const pluginData = {
  key: '.settings.',
  value: 'data'
}

// Key becomes 'settings' instead of '.settings.'
```

### Expected behavior

Plugin data keys should be preserved as-is to maintain backward compatibility. Existing plugins that use keys with consecutive dots or leading/trailing dots should continue to work without modification.

### Additional context

This appears to have started happening recently. Plugins that were working before are now unable to retrieve their stored configuration data because the keys have been normalized/sanitized without the plugin's knowledge.

---
Repository: /testbed
