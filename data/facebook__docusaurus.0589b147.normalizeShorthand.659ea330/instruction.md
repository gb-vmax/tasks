# Bug Report

### Describe the bug

Plugin configuration is not working correctly when using string or array shorthand notation. The plugins fail to load properly and the site build breaks.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    '@docusaurus/plugin-content-docs',
    ['@docusaurus/plugin-content-blog', { blogTitle: 'My Blog' }]
  ]
}
```

When starting the dev server or building the site with the above configuration, the plugins don't resolve correctly. The string shorthand for plugins seems to cause issues, and when using the array format with options, the plugin and options appear to be in the wrong order.

### Expected behavior

Both shorthand formats should work:
1. String format: `'@docusaurus/plugin-content-docs'` should resolve and load the plugin
2. Array format: `['@docusaurus/plugin-content-blog', { options }]` should resolve the plugin with the provided options

The plugins should be loaded in the correct order with their respective configurations applied.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
