# Bug Report

### Describe the bug

When using the docs plugin with multiple content paths, the sidebar file path is being added at the wrong position in the paths to watch array. This causes the file watcher to not properly track changes to the sidebar configuration file.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          sidebarPath: require.resolve('./sidebars.js'),
          include: ['**/*.md', '**/*.mdx'],
        },
      },
    ],
  ],
};
```

Steps to reproduce:
1. Set up a docs plugin with a custom sidebar file
2. Make changes to the sidebar file
3. The changes are not detected in the expected order by the file watcher

### Expected behavior

The sidebar file path should be added to the end of the paths array (using `push`) rather than at the beginning (using `unshift`), so that it maintains the correct watch order for the file watcher.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
