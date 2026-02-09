# Bug Report

### Describe the bug

When configuring plugins using string shorthand notation in `docusaurus.config.js`, the plugin configuration is not being handled correctly. The plugin appears to be initialized but doesn't receive its options properly.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    '@docusaurus/plugin-content-docs',
    // or
    ['@docusaurus/plugin-content-pages', {
      path: 'src/pages',
      routeBasePath: '/'
    }]
  ]
}
```

When using the string shorthand for a plugin (first example), the plugin loads but seems to have unexpected behavior. When using the array format with options (second example), the plugin ignores the provided options and uses defaults instead.

### Expected behavior

- String shorthand should work the same as `['plugin-name', {}]`
- Array format with options should properly pass the options object to the plugin
- Plugin configuration should be normalized consistently

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
