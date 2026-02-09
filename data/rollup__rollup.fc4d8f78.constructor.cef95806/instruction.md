# Bug Report

### Plugin execution order seems incorrect after recent changes

I'm experiencing an issue where plugins are not being executed in the expected order. It looks like the order got reversed somehow.

**Reproduction**

When I configure multiple plugins in my rollup config:

```js
export default {
  input: 'src/index.js',
  plugins: [
    pluginA(),
    pluginB(),
    pluginC()
  ]
}
```

The plugins seem to execute in the wrong order. I expect pluginA to run first, then pluginB, then pluginC, but it appears they're running in reverse or some other unexpected order.

**Expected behavior**

Plugins should execute in the order they are defined in the configuration array. If I have `[pluginA, pluginB, pluginC]`, they should be called in that exact sequence.

**Additional context**

This is causing issues with my build pipeline since some plugins depend on transformations from earlier plugins. The build completes but produces incorrect output because the plugins aren't running in the right order.

---
Repository: /testbed
