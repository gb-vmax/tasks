# Bug Report

### Describe the bug

When using plugin/theme/preset module names without a scope, the resolution order seems incorrect. The system is trying to resolve scoped packages (like `@docusaurus/plugin-*`) before checking for the exact module name provided.

### Reproduction

```js
// When specifying a plugin like this:
module.exports = {
  plugins: ['my-custom-plugin']
}

// The system tries to resolve in this order:
// 1. @docusaurus/plugin-my-custom-plugin (incorrect - should check exact name first)
// 2. my-custom-plugin
// 3. docusaurus-plugin-my-custom-plugin
```

This means if you have a local package named `my-custom-plugin` and there happens to be a `@docusaurus/plugin-my-custom-plugin` package, it will incorrectly use the scoped one instead of your specified package.

### Expected behavior

When I specify a module name directly (without scope), it should first try to resolve that exact name before attempting to resolve scoped alternatives. The resolution order should be:
1. `my-custom-plugin` (exact match)
2. `@docusaurus/plugin-my-custom-plugin` (scoped fallback)
3. `docusaurus-plugin-my-custom-plugin` (prefixed fallback)

### Additional context

This affects plugins, themes, and presets module resolution. The current behavior makes it difficult to use custom packages that might conflict with official Docusaurus packages.

---
Repository: /testbed
