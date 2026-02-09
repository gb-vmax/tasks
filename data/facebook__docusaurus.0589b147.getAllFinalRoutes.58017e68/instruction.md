# Bug Report

### Describe the bug

The `getAllFinalRoutes` function is not returning the correct routes. When I have nested route configurations, routes with subroutes are now being included in the final output even though they shouldn't be.

### Reproduction

```js
const routeConfig = [
  {
    path: '/docs',
    routes: [
      { path: '/docs/intro' },
      { path: '/docs/tutorial' }
    ]
  },
  {
    path: '/blog'
  }
];

const finalRoutes = getAllFinalRoutes(routeConfig);
// Expected: [{ path: '/docs/intro' }, { path: '/docs/tutorial' }, { path: '/blog' }]
// Actual: includes the parent '/docs' route as well
```

The function is supposed to recursively extract only the leaf routes (routes without subroutes), but it's now including parent routes that have children.

### Expected behavior

`getAllFinalRoutes` should return only the final/leaf routes - routes that don't have any subroutes. Parent routes that contain nested routes should not be included in the output.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
