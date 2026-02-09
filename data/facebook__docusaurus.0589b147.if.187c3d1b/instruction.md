# Bug Report

### Describe the bug

When setting `sidebarCollapsible: false` in the docs plugin configuration, the `sidebarCollapsed` option is not being handled correctly. The validation logic appears to be inverted - it's warning and overriding the setting in the wrong condition.

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
          sidebarCollapsed: false,
        },
      },
    ],
  ],
};
```

With this configuration, I'm seeing unexpected behavior where:
1. A warning is logged even though `sidebarCollapsed` is set to `false` (not `true`)
2. The `sidebarCollapsed` value gets changed to `true` instead of staying `false`

### Expected behavior

When `sidebarCollapsible: false` is set:
- If `sidebarCollapsed: true`, it should warn and override to `false` (since you can't collapse something that's not collapsible)
- If `sidebarCollapsed: false`, it should NOT warn and should keep the value as `false`

The current behavior seems backwards - it's checking `if (options.sidebarCollapsed)` when it should probably be checking `if (!options.sidebarCollapsed)` or vice versa.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
