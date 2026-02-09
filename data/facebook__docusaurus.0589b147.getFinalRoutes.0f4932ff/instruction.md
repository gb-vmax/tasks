# Bug Report

### Describe the bug

I'm experiencing an issue with route generation where only the first subroute is being processed for nested route configurations. When I have a route with multiple subroutes, all routes after the first one are being ignored.

### Reproduction

```js
const routeConfig = [
  {
    path: '/docs',
    routes: [
      { path: '/docs/intro' },
      { path: '/docs/tutorial' },
      { path: '/docs/advanced' }
    ]
  }
];

const finalRoutes = getAllFinalRoutes(routeConfig);
// Expected: 3 routes
// Actual: only 1 route (/docs/intro)
```

### Expected behavior

`getAllFinalRoutes` should return all final routes from the route configuration, not just the first subroute. In the example above, it should return an array with all three routes: `/docs/intro`, `/docs/tutorial`, and `/docs/advanced`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken after a recent update. The function used to correctly flatten all nested routes but now only picks up the first one in each routes array.

---
Repository: /testbed
