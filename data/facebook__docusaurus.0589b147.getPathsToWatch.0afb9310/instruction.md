# Bug Report

### Describe the bug

When using the docs plugin with multiple include patterns, the file watcher is not working correctly. It seems like the paths being watched are not flattened properly, causing the dev server to miss changes to documentation files.

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

Steps:
1. Configure the docs plugin with multiple include patterns
2. Start the dev server
3. Edit a markdown file
4. The changes are not detected and hot reload doesn't work

### Expected behavior

The dev server should detect changes to all files matching any of the include patterns and trigger hot reload accordingly.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
