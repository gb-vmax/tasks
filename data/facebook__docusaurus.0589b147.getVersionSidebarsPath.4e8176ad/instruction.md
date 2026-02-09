# Bug Report

### Describe the bug

The versioned sidebars file path is being generated incorrectly. When using a plugin with a custom `pluginId`, the sidebars file is not found in the expected location, causing the versioned docs to fail loading their sidebar configuration.

### Reproduction

```js
// In docusaurus.config.js
plugins: [
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'api-docs',
      path: 'docs-api',
      routeBasePath: 'api',
      versions: {
        current: {
          label: '1.0.0',
        },
      },
    },
  ],
]
```

Steps to reproduce:
1. Configure a docs plugin with a custom `pluginId` (e.g., 'api-docs')
2. Create a versioned docs setup with version name like "1.0.0"
3. Try to load the versioned sidebar

The sidebar file is expected at a different path than where it's actually located, resulting in the sidebar not being loaded properly.

### Expected behavior

The versioned sidebars file path should be constructed consistently, placing the file at:
`versioned_sidebars/version-{versionName}-sidebars.json` 

for the default plugin, and at the appropriate location when using custom plugin IDs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
