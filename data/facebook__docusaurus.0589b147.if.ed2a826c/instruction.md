# Bug Report

### Describe the bug

When using the docs plugin with `sidebarCollapsible: false` in the configuration, the `sidebarCollapsed` option is not being set to its default value correctly. The sidebar behavior is inconsistent when `sidebarCollapsed` is `undefined`.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        sidebarCollapsible: false,
        // sidebarCollapsed is undefined (not set)
      },
    ],
  ],
};
```

### Expected behavior

When `sidebarCollapsible` is set to `false` and `sidebarCollapsed` is not explicitly set (undefined), the plugin should automatically set `sidebarCollapsed` to `false` to maintain consistency. The sidebar should not be collapsible and should remain expanded by default.

### Actual behavior

The default value for `sidebarCollapsed` is not being applied when it's `undefined`, leading to unexpected sidebar behavior.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
