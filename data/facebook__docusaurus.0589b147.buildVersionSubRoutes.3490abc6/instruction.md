# Bug Report

### Describe the bug

After a recent update, the documentation routes are not being generated correctly. When building the site, I'm getting an error about spreading a non-iterable value. It seems like the route structure has changed unexpectedly.

### Reproduction

```js
// When building version routes with sidebar and tags
const routes = await buildVersionRoutes({
  version: myVersion,
  actions: myActions,
  options: myOptions,
  aliasedSource: mySource
});

// Expected: routes should be an array with sidebar route followed by tag routes
// Actual: Error occurs during route building
```

The issue appears when the plugin tries to build routes for a documentation version that has both a sidebar and tags configured.

### Expected behavior

The version routes should be built successfully with the sidebar route as the first element, followed by all tag routes in a flattened array structure.

### System Info
- Docusaurus version: Latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
