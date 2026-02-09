# Bug Report

### Describe the bug

I'm experiencing an issue with route context data in plugins. When a plugin adds a route without a `context` property, the application crashes with an error about trying to access properties of `undefined`.

### Reproduction

Create a plugin that adds a route without context:

```js
export default function myPlugin(context, options) {
  return {
    name: 'my-plugin',
    async contentLoaded({content, actions}) {
      const {addRoute} = actions;
      
      // Add a route without context property
      addRoute({
        path: '/my-page',
        component: '@site/src/components/MyPage',
        exact: true,
      });
    },
  };
}
```

When the site builds or runs in dev mode, it fails because the route configuration tries to access `finalRouteConfig.context` which is undefined.

### Expected behavior

Routes should be added successfully even when the `context` property is not provided. The plugin system should handle cases where `context` is optional or undefined without throwing errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This seems to be a regression as routes without context worked fine in previous versions.

---
Repository: /testbed
