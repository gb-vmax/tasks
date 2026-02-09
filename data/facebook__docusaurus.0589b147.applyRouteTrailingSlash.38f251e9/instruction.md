# Bug Report

### Bug: Infinite recursion when applying trailing slash to nested routes

I'm experiencing an issue with route configuration when using nested routes with trailing slash configuration. The application hangs/crashes when processing routes that have subroutes.

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
const result = applyRouteTrailingSlash(route, { trailingSlash: true })
// Application hangs here
```

### Expected behavior

The function should process nested routes correctly and return a properly formatted route configuration with trailing slashes applied to all paths at every nesting level.

### Actual behavior

The application becomes unresponsive when processing routes with nested subroutes. It appears to get stuck in some kind of loop when trying to apply the trailing slash configuration.

### Environment

- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
