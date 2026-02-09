# Bug Report

### Describe the bug

When using the docs plugin, file watching doesn't work correctly for included documentation files. The dev server doesn't detect changes to markdown files that should be watched according to the `include` patterns configuration.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          include: ['**/*.md', '**/*.mdx'],
          // ... other config
        },
      },
    ],
  ],
};
```

Steps to reproduce:
1. Set up a Docusaurus site with docs plugin
2. Configure multiple include patterns in the docs plugin options
3. Start the dev server
4. Modify a markdown file that matches one of the include patterns
5. The changes are not detected and the page doesn't hot reload

### Expected behavior

All files matching the include patterns should be watched by the dev server. When any of these files are modified, the dev server should detect the change and trigger a hot reload.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
