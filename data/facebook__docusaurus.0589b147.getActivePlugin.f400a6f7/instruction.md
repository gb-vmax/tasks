# Bug Report

### Describe the bug

The active docs plugin is not being selected correctly when multiple plugin instances are configured with different base paths. When navigating to a page under a more specific path like `/android/foo`, the wrong plugin instance is being matched.

### Reproduction

Setup:
1. Configure multiple docs plugin instances with nested paths:
   - Plugin A with path `/`
   - Plugin B with path `/android`

2. Navigate to a page at `/android/foo`

Expected: Plugin B (with path `/android`) should be the active plugin
Actual: Plugin A (with path `/`) is matched instead

This causes issues with version dropdowns, sidebars, and other docs features that rely on the correct plugin context.

### Steps to reproduce

```js
// docusaurus.config.js
plugins: [
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'default',
      path: 'docs',
      routeBasePath: '/',
    },
  ],
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'android',
      path: 'android',
      routeBasePath: '/android',
    },
  ],
]
```

When visiting `/android/getting-started`, the default plugin is selected instead of the android plugin.

### Expected behavior

The plugin with the most specific matching path should be selected. Routes like `/android/foo` should match the `/android` plugin before falling back to the `/` plugin.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
