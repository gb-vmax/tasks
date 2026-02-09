# Bug Report

### Describe the bug

When using a string path to load a plugin, the plugin is not being loaded correctly. The plugin appears to be undefined or not functioning as expected, even though the path is valid and the plugin module exists.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    './my-custom-plugin'
  ]
}
```

When Docusaurus tries to load this plugin, it fails to initialize properly. The plugin path resolves correctly but the actual plugin function/object is not being used.

### Expected behavior

The plugin should be loaded and initialized correctly when specified as a string path. The plugin's functionality should work as expected.

### Additional context

This seems to affect plugins specified as string paths. Plugins specified as functions or arrays with options might not be affected. The issue appears after a recent change in how plugin modules are resolved and loaded.

---
Repository: /testbed
