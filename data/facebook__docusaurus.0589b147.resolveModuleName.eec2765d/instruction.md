# Bug Report

### Describe the bug

Module resolution is broken - Docusaurus is trying to load modules that don't exist instead of the ones that are actually installed. This causes builds to fail with "Cannot find module" errors even when the correct module is present in node_modules.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    '@docusaurus/plugin-content-docs'  // Using shorthand notation
  ]
}
```

When running the build, Docusaurus attempts to resolve a non-existent module path instead of the actual installed plugin.

### Expected behavior

Docusaurus should correctly resolve and load the plugin module that exists in node_modules. The module resolution should find the first module that can actually be required, not the first one that throws an error.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Package manager: npm

---
Repository: /testbed
