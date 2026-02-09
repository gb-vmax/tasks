# Bug Report

### Describe the bug

I'm experiencing an issue with route processing where nested routes are not being flattened correctly. When I have a route configuration with multiple levels of nested subroutes, the final route structure contains unexpected nested arrays instead of a flat list of routes.

### Reproduction

```js
const routeConfig = [
  {
    path: '/docs',
    routes: [
      {
        path: '/docs/intro',
        component: 'intro.js'
      },
      {
        path: '/docs/guides',
        routes: [
          {
            path: '/docs/guides/getting-started',
            component: 'getting-started.js'
          }
        ]
      }
    ]
  }
];

const finalRoutes = getAllFinalRoutes(routeConfig);
// Returns nested arrays instead of flat route list
// Expected: array of route objects
// Actual: array containing nested structures
```

### Expected behavior

`getAllFinalRoutes` should return a flat array of all final routes (routes without subroutes), regardless of how deeply nested the original route configuration is.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
