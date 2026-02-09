# Bug Report

### Describe the bug

When specifying a plugin or theme by its exact module name (without the `@docusaurus/` or `docusaurus-` prefix), Docusaurus no longer resolves it correctly. The module resolution seems to only check for prefixed variations now.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    'my-custom-plugin', // This exact name is not resolved anymore
  ],
};
```

If you have a plugin installed as `my-custom-plugin` (the exact package name), Docusaurus fails to find it and only tries to resolve:
- `@docusaurus/plugin-my-custom-plugin`
- `docusaurus-plugin-my-custom-plugin`

But it doesn't try the exact name `my-custom-plugin` that was specified.

### Expected behavior

Docusaurus should first try to resolve the exact module name as provided before attempting to add prefixes. This was working in previous versions where you could specify custom plugins/themes by their exact npm package names.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
