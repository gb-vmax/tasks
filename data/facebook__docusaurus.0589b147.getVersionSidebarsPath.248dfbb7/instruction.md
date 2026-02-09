# Bug Report

### Describe the bug

When using a non-default plugin ID with versioned docs, the sidebars file path is generated incorrectly. The plugin is looking for the sidebars file in the wrong location, causing versioned sidebars to not be found.

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
1. Set up a docs plugin with a custom plugin ID (e.g., `id: 'community'`)
2. Create a versioned docs structure with sidebars
3. The plugin fails to locate the versioned sidebars file

Expected file path: `versioned_sidebars/version-1.0.0-community-sidebars.json`
Actual file path being searched: `versioned_sidebars_community/version-1.0.0-sidebars.json`

### Expected behavior

The plugin should correctly locate versioned sidebars files when using a custom plugin ID. The plugin ID should be appended to the version name in the filename, not to the directory name.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
