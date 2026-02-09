# Bug Report

### Describe the bug

The `getAllFinalRoutes` function is returning incorrect results. When I have a route configuration with nested subroutes, the function is now returning parent routes that have children instead of just the final leaf routes. It's also excluding routes that don't have any subroutes at all.

### Reproduction

```js
const routeConfig = [
  {
    path: '/docs',
    component: DocsLayout,
    routes: [
      {
        path: '/docs/intro',
        component: IntroPage
      }
    ]
  },
  {
    path: '/about',
    component: AboutPage
  }
];

const finalRoutes = getAllFinalRoutes(routeConfig);
// Expected: [{ path: '/docs/intro', ... }, { path: '/about', ... }]
// Actual: [{ path: '/docs', routes: [...], ... }, { path: '/docs/intro', ... }]
// The '/about' route is missing and '/docs' parent route is incorrectly included
```

### Expected behavior

`getAllFinalRoutes` should return only the final/leaf routes (routes without any subroutes). Parent routes that contain nested routes should not be included in the result. Routes without children should be included as they are final routes themselves.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
