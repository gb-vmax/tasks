# Bug Report

### Describe the bug

When trying to use plugin/theme/preset shorthand names in Docusaurus config, I'm getting unexpected behavior where it seems like the module resolution is returning an array instead of the actual module name. This breaks the plugin loading process.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    '@docusaurus/preset-classic'
  ],
  themes: [
    'my-custom-theme'
  ]
}
```

When running the site, the module resolution seems to be broken. Instead of resolving to the correct module name, it appears to be using an array which causes issues downstream.

### Expected behavior

The module shorthand resolution should return the first matching module name string that can be resolved, not an array. For example, when I specify `'@docusaurus/preset-classic'`, it should resolve to that exact package name if it's installed.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems like a regression - module resolution was working fine before. The config hasn't changed but suddenly plugins/themes aren't loading correctly.

---
Repository: /testbed
