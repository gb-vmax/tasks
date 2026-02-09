# Bug Report

### Describe the bug

When using a custom plugin ID for the docs plugin, the versions JSON file is being looked up in the wrong location. The plugin is trying to find the file at a path like `[siteDir]/[pluginId]/versions.json` instead of the correct path `[siteDir]/[pluginId]_versions.json`.

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
1. Set up a docs plugin with a custom plugin ID (e.g., `community`)
2. Create a versions file at the expected location: `community_versions.json`
3. Try to build or start the site
4. The plugin fails to find the versions file

### Expected behavior

The plugin should look for the versions file at `[siteDir]/community_versions.json` (using the `addPluginIdPrefix` helper to generate the correct filename), not at `[siteDir]/community/versions.json`.

For a plugin with ID `community`, the expected path should be:
- `community_versions.json` ✓
- NOT `community/versions.json` ✗

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
