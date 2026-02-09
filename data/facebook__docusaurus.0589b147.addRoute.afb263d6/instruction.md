# Bug Report

### Describe the bug

I'm experiencing an issue where only the last route added by a plugin is being registered. When a plugin calls `addRoute()` multiple times to register different routes, only the final route appears to be available while all previously added routes are lost.

### Reproduction

```js
// In a plugin's contentLoaded lifecycle
async contentLoaded({content, actions}) {
  const {addRoute} = actions;
  
  // Add first route
  addRoute({
    path: '/docs/intro',
    component: '@site/src/components/Intro.js',
  });
  
  // Add second route
  addRoute({
    path: '/docs/tutorial',
    component: '@site/src/components/Tutorial.js',
  });
  
  // Add third route
  addRoute({
    path: '/docs/advanced',
    component: '@site/src/components/Advanced.js',
  });
}
```

### Expected behavior

All three routes should be registered and accessible:
- `/docs/intro`
- `/docs/tutorial`
- `/docs/advanced`

### Actual behavior

Only the last route (`/docs/advanced`) is registered. The first two routes (`/docs/intro` and `/docs/tutorial`) return 404 errors when accessed.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems like a regression as this was working fine in previous versions. Any plugin that registers multiple routes is affected by this issue.

---
Repository: /testbed
