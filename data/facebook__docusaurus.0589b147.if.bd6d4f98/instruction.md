# Bug Report

### Describe the bug

When using string-based plugin imports in the Docusaurus config, the plugin system is not resolving the correct paths. The plugin module path and entry path seem to be swapped, causing issues with plugin loading.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    './my-custom-plugin',
    // or
    '@docusaurus/plugin-content-docs'
  ]
}
```

When the config is loaded, the plugin paths are incorrectly assigned:
- The `pluginModule.path` receives the resolved absolute path instead of the import string
- The `entryPath` receives the import string instead of the resolved absolute path

This causes downstream issues when the plugin system tries to reference these paths.

### Expected behavior

The plugin configuration should correctly map:
- `pluginModule.path` should contain the original import string (e.g., `'./my-custom-plugin'`)
- `entryPath` should contain the resolved absolute path from `pluginRequire.resolve()`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
