# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where the wrong plugin instance is being selected when navigating to nested routes. It seems like the route matching logic is picking the wrong plugin when multiple plugins have overlapping path prefixes.

### Reproduction

Setup:
```js
// Multiple docs plugin instances with different base paths
plugins: [
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'root',
      path: 'docs',
      routeBasePath: '/',
    },
  ],
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'android',
      path: 'docs-android',
      routeBasePath: '/android',
    },
  ],
]
```

Steps to reproduce:
1. Navigate to `/android/foo` 
2. The active plugin should be the 'android' instance
3. Instead, it appears to be matching the 'root' instance with path `/`

### Expected behavior

When navigating to `/android/foo`, the docs plugin with `routeBasePath: '/android'` should be selected as the active plugin, not the one with `routeBasePath: '/'`. The more specific route should take precedence over the generic one.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
