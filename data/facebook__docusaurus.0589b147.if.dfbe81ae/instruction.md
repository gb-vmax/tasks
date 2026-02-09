# Bug Report

### Describe the bug

When setting `sidebarFilePath` to an empty string (`''`), the sidebars are unexpectedly disabled instead of being treated as an invalid path. This causes the documentation to render without any sidebar navigation.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: '', // Empty string
        },
      },
    ],
  ],
};
```

### Expected behavior

An empty string should either:
1. Throw an error indicating an invalid path, or
2. Be treated differently from `false` (which explicitly disables sidebars)

Currently, passing an empty string has the same effect as passing `false`, which disables the sidebars entirely. This is confusing because an empty string is likely a configuration mistake rather than an intentional choice to disable sidebars.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
