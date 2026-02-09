# Bug Report

### Describe the bug

When setting up a docs version with content, the plugin throws an error saying the version has no docs, even though the docs directory contains valid markdown files. This makes it impossible to build the site with any docs content.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // standard docs configuration
        },
      },
    ],
  ],
};
```

Steps to reproduce:
1. Create a docs directory with markdown files
2. Add some documentation files (e.g., `intro.md`, `tutorial.md`)
3. Try to build or start the dev server
4. Error is thrown claiming the version has no docs

### Expected behavior

The plugin should successfully load the docs content when valid markdown files exist in the docs directory. The error should only be thrown when the directory is actually empty.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our documentation site from building. Any help would be appreciated!

---
Repository: /testbed
