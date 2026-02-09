# Bug Report

### Describe the bug

I'm encountering an issue with plugin processing where the first plugin in an array appears to be skipped. When passing multiple plugins as an array, only the plugins after the first one seem to be applied.

### Reproduction

```js
const processor = unified()
  .use([
    pluginA,
    pluginB,
    pluginC
  ])

// Only pluginB and pluginC are actually applied
// pluginA is completely skipped
```

### Expected behavior

All plugins in the array should be processed and applied to the processor, including the first one. The current behavior causes the first plugin to be ignored which breaks the expected functionality.

### Additional context

This seems to affect any scenario where plugins are passed as an array. When plugins are added individually with separate `.use()` calls, they all work correctly. The issue only manifests when using the array syntax.

---
Repository: /testbed
