# Bug Report

### Describe the bug

When using plugin/theme/preset shorthand names in Docusaurus configuration, the module resolution is not working correctly. Instead of resolving to the first valid module that can be required, it always returns the first pattern regardless of whether it can actually be resolved.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  themes: ['classic'], // shorthand for @docusaurus/theme-classic
  plugins: ['content-docs'], // shorthand for @docusaurus/plugin-content-docs
};
```

When the shorthand module name is provided and multiple patterns are generated (e.g., `classic`, `@docusaurus/theme-classic`, `docusaurus-theme-classic`), the resolution tries to find which one is actually installed but then returns the wrong pattern.

### Expected behavior

The module resolver should return the first pattern that successfully resolves (i.e., the module that is actually installed), not just the first pattern in the list.

For example, if I use the shorthand `'classic'` for a theme, and the actual installed package is `@docusaurus/theme-classic`, the resolver should return `@docusaurus/theme-classic`, not `classic`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to affect all module types (plugins, themes, and presets) when using shorthand notation.

---
Repository: /testbed
