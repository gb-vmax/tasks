# Bug Report

### Describe the bug

When configuring a docs plugin without specifying a `sidebarPath` (leaving it undefined), the sidebar is not being auto-generated as expected. Instead of getting the default auto-generated sidebars, the sidebar appears to be empty or missing.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // sidebarPath is intentionally undefined to use auto-generated sidebars
          // sidebarPath: undefined,
        },
      },
    ],
  ],
};
```

Steps to reproduce:
1. Create a Docusaurus site with the docs plugin
2. Don't specify a `sidebarPath` option (or explicitly set it to `undefined`)
3. Add some markdown files to the docs folder
4. Build or start the dev server
5. Navigate to the docs - the sidebar doesn't appear or is empty

### Expected behavior

When `sidebarPath` is undefined, Docusaurus should fall back to auto-generating the sidebars based on the file structure in the docs directory. This was the documented default behavior.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
