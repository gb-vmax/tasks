# Bug Report

### Describe the bug

When using scoped package names (starting with `@`) in plugin/theme/preset configurations, the module resolution is not working correctly. The shorthand expansion doesn't include the original scoped package name in the resolution patterns, causing failures when trying to use packages with their full scoped names.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  plugins: [
    '@myorg/my-plugin'  // This should resolve to @myorg/my-plugin
  ]
}
```

When specifying a scoped package like `@myorg/my-plugin`, the module resolution fails because it only tries to resolve to `@myorg/docusaurus-plugin-my-plugin` but never attempts the original name `@myorg/my-plugin`.

### Expected behavior

The module shorthand should include the original scoped package name in its resolution patterns. For example, `@myorg/my-plugin` should try to resolve:
1. `@myorg/my-plugin` (original name)
2. `@myorg/docusaurus-plugin-my-plugin` (expanded shorthand)

This way, both official Docusaurus plugins and custom scoped packages work correctly.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
