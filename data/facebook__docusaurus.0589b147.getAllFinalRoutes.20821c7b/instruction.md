# Bug Report

### Describe the bug

I'm experiencing an issue with route generation where nested routes are being returned incorrectly. When I have a route configuration with subroutes, the parent route itself is being included in the final routes array instead of just the leaf routes.

### Reproduction

```js
const routeConfig = [
  {
    path: '/docs',
    routes: [
      { path: '/docs/intro' },
      { path: '/docs/tutorial' }
    ]
  }
];

const finalRoutes = getAllFinalRoutes(routeConfig);
// Expected: [{ path: '/docs/intro' }, { path: '/docs/tutorial' }]
// Actual: Returns the parent route { path: '/docs', routes: [...] }
```

### Expected behavior

The `getAllFinalRoutes` function should recursively traverse the route configuration and return only the leaf routes (routes without subroutes). Parent routes that have child routes should not be included in the final output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken route generation in my project - pages that should be accessible at leaf route paths are not being created properly.

---
Repository: /testbed
