# Bug Report

### Describe the bug

When setting `sidebarCollapsible: false` in the docs plugin configuration without explicitly setting `sidebarCollapsed`, the sidebar items are not defaulting to the collapsed state as expected. The sidebar remains expanded even though `sidebarCollapsible` is set to false.

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
          // sidebarCollapsed is not set (undefined)
        },
      },
    ],
  ],
};
```

### Expected behavior

When `sidebarCollapsible` is set to `false` and `sidebarCollapsed` is not explicitly defined, the sidebar should default to collapsed state (`sidebarCollapsed: false`). This would be consistent behavior since non-collapsible sidebars should start in a collapsed state.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
