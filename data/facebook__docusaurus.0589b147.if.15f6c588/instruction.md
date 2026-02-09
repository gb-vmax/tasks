# Bug Report

### Describe the bug

When configuring the docs plugin with `sidebarCollapsible: false` and `sidebarCollapsed: true`, the validation logic appears to be incorrect. The sidebar ends up being collapsed even though collapsibility is disabled, which doesn't make sense.

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
          sidebarCollapsed: true,
        },
      },
    ],
  ],
};
```

### Expected behavior

When `sidebarCollapsible: false`, the `sidebarCollapsed: true` setting should be ignored and the sidebar should remain expanded (not collapsed). The current behavior seems to do the opposite - it collapses the sidebar even when collapsibility is disabled.

A warning message is shown about the inconsistent config, but the resulting behavior doesn't match what the warning suggests will happen.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
