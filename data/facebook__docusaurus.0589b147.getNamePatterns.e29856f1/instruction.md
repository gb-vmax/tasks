# Bug Report

### Describe the bug

When using plugin/theme shorthand names in Docusaurus configuration, the module resolution order seems to have changed. Specifically, when I specify a plugin using just the package name (without the `@docusaurus/` prefix or `docusaurus-plugin-` prefix), it's no longer being resolved correctly.

### Reproduction

In `docusaurus.config.js`:

```js
module.exports = {
  plugins: [
    'my-custom-plugin'  // Previously worked, now fails to resolve
  ]
}
```

The plugin `my-custom-plugin` exists in `node_modules` but Docusaurus is trying to resolve `@docusaurus/plugin-my-custom-plugin` first instead of checking for the exact module name.

### Expected behavior

When using a bare module name like `'my-custom-plugin'`, Docusaurus should check if that exact package exists before trying to prepend `@docusaurus/` or `docusaurus-plugin-` prefixes. This was the previous behavior and allowed for custom plugins without the Docusaurus naming convention.

The resolution should prioritize:
1. Exact module name match
2. Official `@docusaurus/` scoped packages
3. Community `docusaurus-*` prefixed packages

### System Info

- Docusaurus version: latest
- Node version: 18.x
- Package manager: npm

---
Repository: /testbed
