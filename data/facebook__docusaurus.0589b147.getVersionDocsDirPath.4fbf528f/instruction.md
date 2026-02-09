# Bug Report

### Describe the bug

The versioned docs directory path is being constructed incorrectly when using a plugin with a custom `pluginId`. The plugin ID prefix is being applied to the wrong part of the path, causing Docusaurus to look for versioned documentation in the wrong location.

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
        routeBasePath: 'community',
        // ... other options
      },
    ],
  ],
};
```

With this configuration and versioned docs:
1. Create a versioned docs folder structure
2. Add version 1.0.0 documentation
3. Try to access the versioned documentation

Expected path: `versioned_docs/version-1.0.0_community/`
Actual path being searched: `versioned_docs_community/version-1.0.0/`

This results in Docusaurus being unable to find the versioned documentation files for plugins with custom IDs.

### Expected behavior

The versioned docs directory should be constructed as `versioned_docs/version-{versionName}_{pluginId}/` when a custom plugin ID is provided, allowing multiple doc plugins to maintain their own versioned documentation in separate directories.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
