# Bug Report

### Describe the bug

When setting `sidebarCollapsible: false` in the docs plugin configuration without explicitly setting `sidebarCollapsed`, the sidebar items are being collapsed by default instead of expanded. This is the opposite of the expected behavior.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarCollapsible: false,
          // sidebarCollapsed not set (undefined)
        },
      },
    ],
  ],
};
```

After starting the dev server, all sidebar categories appear collapsed even though `sidebarCollapsible` is set to `false`.

### Expected behavior

When `sidebarCollapsible` is set to `false` and `sidebarCollapsed` is not explicitly defined, the sidebar items should default to expanded (not collapsed). This makes sense because if items aren't collapsible, they should be shown expanded by default.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
