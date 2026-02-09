# Bug Report

### Describe the bug

When setting `sidebarCollapsible: false` and `sidebarCollapsed: true` together in the docs plugin configuration, the warning message says that `sidebarCollapsed: true` will be ignored, but the actual behavior is inconsistent with this warning.

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

According to the warning message that appears in the console:
```
The docs plugin config is inconsistent. It does not make sense to use sidebarCollapsible: false and sidebarCollapsed: true at the same time. sidebarCollapsed: true will be ignored.
```

The `sidebarCollapsed` option should be ignored (treated as if it wasn't set), but instead it seems to be set to `false` rather than being truly ignored/undefined.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
