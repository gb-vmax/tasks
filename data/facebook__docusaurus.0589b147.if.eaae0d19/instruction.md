# Bug Report

### Describe the bug

When retrieving plugin metadata, the plugin name is returning the version number instead of the actual package name. This appears to affect plugin identification and metadata display.

### Reproduction

```js
// In a plugin's package.json:
{
  "name": "@docusaurus/plugin-content-docs",
  "version": "2.4.0"
}

// When calling getPluginVersion/metadata:
// Expected: name = "@docusaurus/plugin-content-docs"
// Actual: name = "2.4.0"
```

### Expected behavior

The plugin name should return the `name` field from package.json, not the `version` field.

### System Info
- Docusaurus version: 2.x
- Node version: 18.x

---
Repository: /testbed
