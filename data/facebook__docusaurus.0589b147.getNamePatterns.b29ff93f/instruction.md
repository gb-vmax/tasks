# Bug Report

### Describe the bug

When using shorthand module names for Docusaurus plugins, the resolution order seems to have changed and is now prioritizing scoped package names over the exact module name provided. This causes issues when you have both a scoped package and a non-scoped package with the same name.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    'my-plugin'  // This should resolve to 'my-plugin' first, but now resolves to '@docusaurus/plugin-my-plugin' first
  ]
}
```

If you have a local plugin named `my-plugin` and also have `@docusaurus/plugin-my-plugin` installed, the system will now pick the scoped version instead of the exact name you specified.

Similarly for scoped packages:
```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    '@myorg/custom'  // Should resolve to '@myorg/custom' first, but resolves to '@myorg/docusaurus-plugin-custom' first
  ]
}
```

### Expected behavior

When specifying a module name, the exact name should be tried first before falling back to Docusaurus naming conventions. This was the previous behavior and changing it breaks existing configurations that rely on the resolution order.

For example:
- `'my-plugin'` should try `'my-plugin'` before `'@docusaurus/plugin-my-plugin'`
- `'@myorg/custom'` should try `'@myorg/custom'` before `'@myorg/docusaurus-plugin-custom'`

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
