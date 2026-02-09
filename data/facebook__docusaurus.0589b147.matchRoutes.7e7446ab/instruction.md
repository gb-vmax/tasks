# Bug Report

### Describe the bug

Routes are not being matched properly after a recent change. When trying to navigate to valid routes, the system is not finding any matches even though the routes are correctly configured.

### Reproduction

```js
const routeConfig = [
  { path: '/docs', component: DocsPage },
  { path: '/blog', component: BlogPage },
  { path: '/about', component: AboutPage }
];

// This should match the route but returns empty array
const matches = matchRoutes(routeConfig, '/docs');
console.log(matches); // Expected: array with matched route, Actual: []

// Same issue with other paths
const blogMatches = matchRoutes(routeConfig, '/blog');
console.log(blogMatches); // Expected: array with matched route, Actual: []
```

### Expected behavior

When a valid pathname is provided that matches a configured route, `matchRoutes` should return an array containing the matched route(s). Currently it's returning an empty array for all valid routes.

This is breaking navigation throughout the site as no routes are being matched, even though the route configuration is correct.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
