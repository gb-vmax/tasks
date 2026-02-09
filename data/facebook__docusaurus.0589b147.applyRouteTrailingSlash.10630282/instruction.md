# Bug Report

### Describe the bug

When using nested routes with trailing slash configuration, the trailing slash settings are not being applied correctly to subroutes. Instead of using the original `params` for subroutes, it seems like the parent route object is being passed down, causing incorrect path transformations.

### Reproduction

```js
const route = {
  path: '/docs/',
  routes: [
    { path: '/docs/intro/' },
    { path: '/docs/tutorial/' }
  ]
};

const params = {
  trailingSlash: false,
  baseUrl: '/'
};

const result = applyRouteTrailingSlash(route, params);
// Subroutes don't get the trailing slash removed as expected
```

### Expected behavior

Subroutes should inherit the same trailing slash parameters as the parent route. If `trailingSlash: false` is configured, all nested routes should have their trailing slashes removed consistently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
