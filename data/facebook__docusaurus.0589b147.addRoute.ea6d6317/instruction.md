# Bug Report

### Describe the bug

Routes are not being registered correctly in plugins. When a plugin calls `addRoute()`, the route configuration structure appears to be malformed, causing the entire route config object to be nested under the `context` property instead of being spread at the top level.

### Reproduction

```js
// In a Docusaurus plugin
export default function myPlugin(context, options) {
  return {
    name: 'my-plugin',
    async contentLoaded({content, actions}) {
      const {addRoute} = actions;
      
      addRoute({
        path: '/my-page',
        component: '@site/src/components/MyPage',
        exact: true,
        context: {
          someData: 'test'
        }
      });
    },
  };
}
```

After this runs, the route config doesn't have the expected structure. Properties like `path`, `component`, and `exact` are not at the top level where they should be.

### Expected behavior

The route configuration should maintain its structure with `path`, `component`, `exact` and other route properties at the top level, while `context` should contain the plugin-specific data and metadata.

The expected structure should be:
```js
{
  path: '/my-page',
  component: '@site/src/components/MyPage',
  exact: true,
  context: {
    data: { someData: 'test' },
    plugin: '...'
  }
}
```

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
