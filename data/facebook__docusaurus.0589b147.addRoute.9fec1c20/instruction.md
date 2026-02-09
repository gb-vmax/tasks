# Bug Report

### Describe the bug

When using `addRoute()` in a plugin's `contentLoaded` lifecycle, the route configuration properties are not being passed through correctly. All route properties like `path`, `component`, `exact`, etc. are being dropped, and only the `context` field is preserved.

### Reproduction

```js
// In a Docusaurus plugin
async contentLoaded({content, actions}) {
  const {addRoute} = actions;
  
  addRoute({
    path: '/my-custom-page',
    component: '@site/src/components/MyPage.js',
    exact: true,
    context: {
      customData: 'test'
    }
  });
}
```

After calling `addRoute()`, the resulting route config only contains the `context` property. The `path`, `component`, and `exact` properties are missing, causing the route to not work properly.

### Expected behavior

The route should be created with all the properties from the initial config (`path`, `component`, `exact`, etc.) along with the enhanced `context` that includes the plugin information.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
