# Bug Report

### Describe the bug

When trying to use module shorthand syntax in Docusaurus, the plugin resolution is completely broken. Instead of finding and using installed packages, it throws an error claiming the module cannot be resolved even when the package is properly installed.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    '@docusaurus/plugin-content-docs'  // Using shorthand
  ]
}
```

After starting the dev server, I get an error message saying:
```
Docusaurus was unable to resolve the "@docusaurus/plugin-content-docs" plugin. Make sure one of the following packages are installed:
- @docusaurus/plugin-content-docs
```

But the package IS installed! I can see it in my `node_modules` and it's listed in `package.json`.

### Expected behavior

The module shorthand should work correctly and resolve installed packages without throwing errors. This used to work fine in previous versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- Package manager: npm

This is blocking me from using any plugins with shorthand syntax. Any help would be appreciated!

---
Repository: /testbed
