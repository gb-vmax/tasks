# Bug Report

### Describe the bug

Module resolution is not working correctly when using plugin shorthand notation. When I specify a plugin without a scope (e.g., `'classic'`), it's no longer finding the correct package.

### Reproduction

In my `docusaurus.config.js`:

```js
module.exports = {
  plugins: [
    'classic'
  ]
}
```

The plugin resolution fails to find `@docusaurus/plugin-classic` or `docusaurus-plugin-classic`. It seems like the module name patterns aren't being generated correctly.

Also seeing issues with scoped packages - when using something like `@myorg/myplugin`, the package name part after the slash isn't being extracted properly.

### Expected behavior

The shorthand should resolve to the full package names:
- `'classic'` should try `@docusaurus/plugin-classic` and `docusaurus-plugin-classic`
- `'@myorg/myplugin'` should properly split the scope and package name

This was working fine in previous versions.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
