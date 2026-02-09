# Bug Report

### Describe the bug

When configuring routes with nested subroutes, the trailing slash configuration is not being applied recursively to deeply nested route paths. Only the first level of subroutes gets the trailing slash treatment, but any routes nested beyond that level don't respect the `trailingSlash` setting.

### Reproduction

```js
const routes = {
  path: '/docs',
  routes: [
    {
      path: '/docs/intro',
      routes: [
        {
          path: '/docs/intro/getting-started'
        }
      ]
    }
  ]
}

// With trailingSlash: true
// Expected: /docs/, /docs/intro/, /docs/intro/getting-started/
// Actual: /docs/, /docs/intro/, /docs/intro/getting-started (no trailing slash on deeply nested routes)
```

### Expected behavior

All nested routes at any depth should have the trailing slash configuration applied consistently, not just the immediate children of the root route.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
