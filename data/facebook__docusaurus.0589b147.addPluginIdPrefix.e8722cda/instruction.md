# Bug Report

### Describe the bug

When using a non-default plugin ID with the docs plugin, the versioned directories and files are not being prefixed correctly. The plugin ID prefix is missing when it should be present, and appears when it shouldn't be.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'community',
        path: 'community',
        // ... other options
      },
    ],
  ],
};
```

Steps to reproduce:
1. Set up a docs plugin instance with a custom plugin ID (e.g., `'community'`)
2. Create versioned docs for this instance
3. Check the generated directory structure

### Expected behavior

For a plugin with ID `'community'`, the versioned directories should be prefixed like:
- `community_versioned_docs/`
- `community_versioned_sidebars/`
- `community_versions.json`

For the default plugin instance, no prefix should be added.

### Actual behavior

The prefix logic appears to be inverted - the default instance gets prefixed when it shouldn't, and custom instances don't get the prefix when they should.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
