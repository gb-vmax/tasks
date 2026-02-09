# Bug Report

### Describe the bug

When setting `sidebarCollapsible: false` in the docs plugin configuration without explicitly setting `sidebarCollapsed`, the sidebar items are not behaving as expected. The default behavior seems to have changed.

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
          // sidebarCollapsed not explicitly set
        },
      },
    ],
  ],
};
```

### Expected behavior

When `sidebarCollapsible` is set to `false` and `sidebarCollapsed` is not explicitly defined, the sidebar should default to an expanded state (not collapsed). This was the previous behavior and makes sense since non-collapsible sidebars should show their content by default.

### Actual behavior

The sidebar appears to be treating the undefined `sidebarCollapsed` value differently than before, which is causing unexpected default behavior.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
