# Bug Report

### Describe the bug

When setting `sidebar: false` in the plugin options to disable sidebars, the sidebars are still being generated and displayed. It seems like the configuration is being ignored and sidebars appear even when explicitly disabled.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs',
        path: 'docs',
        sidebar: false, // This should disable sidebars
      },
    ],
  ],
};
```

After setting `sidebar: false`, I expected no sidebars to be rendered, but they still show up on the documentation pages.

### Expected behavior

When `sidebar: false` is set in the plugin configuration, no sidebars should be generated or displayed. The docs pages should render without any sidebar navigation.

### System Info
- Docusaurus version: 2.x
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
