# Bug Report

### Describe the bug

When using a string-based plugin configuration (e.g., `plugins: ["./my-plugin"]`), the plugin fails to load correctly. The plugin module import path is being incorrectly assigned, causing the plugin system to break.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    './my-custom-plugin'  // String-based plugin reference
  ]
}
```

When Docusaurus tries to load the plugin, it appears to be using the wrong value for the plugin module path. Instead of using the original import string, it seems to be referencing something else entirely.

### Expected behavior

The plugin should load correctly when specified as a string path. The plugin module's path should be set to the original import string (e.g., `"./my-custom-plugin"`), not to the resolved module's default export.

### Additional context

This affects the basic plugin loading mechanism when using string-based plugin configurations. The issue appears to be in how the plugin module metadata is being constructed during normalization.

---
Repository: /testbed
