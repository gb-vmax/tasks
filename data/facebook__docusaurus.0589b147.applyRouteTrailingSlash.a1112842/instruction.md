# Bug Report

### Describe the bug

I'm experiencing an issue with nested routes where subroutes are being removed unexpectedly. When a route has both a `path` and nested `routes`, the nested routes seem to disappear during route configuration processing.

### Reproduction

```js
const route = {
  path: '/docs',
  routes: [
    { path: '/docs/intro' },
    { path: '/docs/tutorial' }
  ]
}

// After applying route configuration
// The nested routes array becomes undefined
```

### Expected behavior

Routes with both a `path` property and nested `routes` should preserve their subroutes. The nested route structure should remain intact regardless of whether the parent route has a path defined.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking my documentation site's navigation as all nested routes are being stripped out. Any help would be appreciated!

---
Repository: /testbed
