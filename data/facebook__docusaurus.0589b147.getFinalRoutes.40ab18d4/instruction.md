# Bug Report

### Describe the bug

The `getAllFinalRoutes` function is returning incorrect results when processing nested route configurations. Instead of returning only the final/leaf routes (routes with no subroutes), it's now including parent routes in the output and wrapping individual routes in extra arrays.

### Reproduction

```js
const routeConfig = [
  {
    path: '/parent',
    routes: [
      { path: '/parent/child1' },
      { path: '/parent/child2' }
    ]
  },
  { path: '/standalone' }
];

const finalRoutes = getAllFinalRoutes(routeConfig);
// Expected: [{ path: '/parent/child1' }, { path: '/parent/child2' }, { path: '/standalone' }]
// Actual: includes parent route and has nested array structure
```

### Expected behavior

The function should only return routes that have no subroutes (leaf routes). Parent routes with nested `routes` should not be included in the output, and the result should be a flat array of route objects.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
