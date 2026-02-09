# Bug Report

### Describe the bug

When using multiple MDX plugins, the first plugin in the array is being skipped and not applied. Only plugins at index 1 and beyond are actually being processed.

### Reproduction

```js
const processor = unified()
  .use(remarkMdx)
  .use([
    pluginA,  // This plugin is skipped
    pluginB,  // This one works
    pluginC   // This one works too
  ])

// Only pluginB and pluginC are applied, pluginA is ignored
```

### Expected behavior

All plugins in the array should be processed and applied in order, including the first one at index 0.

### Additional context

This seems to affect any workflow where plugins are passed as an array. If you pass plugins individually with separate `.use()` calls, they all work fine. The issue only appears when using an array of plugins.

---
Repository: /testbed
