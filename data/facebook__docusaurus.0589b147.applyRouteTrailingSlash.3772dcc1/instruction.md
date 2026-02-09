# Bug Report

### Describe the bug

When configuring routes with nested subroutes, the trailing slash configuration is not being applied to child routes. The parent route gets the trailing slash applied correctly, but nested routes under it remain unchanged.

### Reproduction

```js
const route = {
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

// Apply trailing slash configuration
const result = applyRouteTrailingSlash(route, trailingSlashParams)

// Expected: all paths should have trailing slashes applied
// Actual: only the top-level path is modified, nested routes are ignored
```

### Expected behavior

All nested routes should have the trailing slash configuration applied recursively, not just the top-level route. If I configure trailing slashes to be added/removed, this should affect the entire route tree.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
