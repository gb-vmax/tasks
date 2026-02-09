# Bug Report

### Describe the bug

I'm experiencing an issue with plugin resolution when using the `skip` parameter in `this.resolve()`. It seems like plugins are not being skipped correctly when resolving module IDs.

### Reproduction

```js
// In a plugin's resolveId hook
const result = await this.resolve(
  './some-module',
  importer,
  {
    skip: [{ plugin: currentPlugin, source: './some-module', importer }]
  }
);
```

When I try to skip a specific plugin during resolution, the plugin is still being called instead of being skipped. This causes infinite recursion in some cases where a plugin needs to call `this.resolve()` for the same module without re-entering itself.

### Expected behavior

When a plugin is added to the `skip` array with matching `source` and `importer`, that plugin should be skipped during the resolution process. The resolution should proceed to the next plugin in the chain without calling the skipped plugin's `resolveId` hook.

### Additional context

This is particularly problematic when building custom resolver plugins that need to delegate to other plugins conditionally. The skip mechanism should allow a plugin to avoid infinite loops when calling `this.resolve()` with the same parameters.

---
Repository: /testbed
