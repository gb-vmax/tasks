# Bug Report

### Describe the bug

I'm experiencing an issue with plugin loading in Docusaurus where plugins specified as string paths are not being resolved correctly. When I configure a plugin using a string path (like `"./plugin"` or a module name), the plugin fails to load properly.

### Reproduction

In `docusaurus.config.js`:

```js
module.exports = {
  plugins: [
    './my-custom-plugin',
    // or
    '@docusaurus/plugin-content-docs'
  ]
}
```

When starting the dev server or building the site, the plugin doesn't load as expected. The issue seems to affect both local file paths and npm package references when they're specified as strings in the plugins array.

### Expected behavior

Plugins specified as string paths should be resolved and loaded correctly, whether they're:
- Local file paths (e.g., `"./plugins/my-plugin"`)
- Node module names (e.g., `"@docusaurus/plugin-content-docs"`)

The plugin resolution should work the same way it did in previous versions.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
