# Bug Report

### Describe the bug

I'm experiencing an issue with plugin registration when using the unified/MDX processor. When I try to register the same plugin multiple times with different configurations, the plugin settings aren't being merged correctly. It seems like the first plugin in the attachers array is being skipped during the lookup process.

### Reproduction

```js
const processor = unified()
  .use(somePlugin, { option1: 'value1' })
  .use(somePlugin, { option2: 'value2' });

// Expected: plugin should have both option1 and option2 merged
// Actual: The plugin configuration is not updated correctly
```

When trying to add a plugin that's already registered at index 0, it doesn't get found and ends up being added as a duplicate instead of merging the options.

### Expected behavior

When the same plugin is registered multiple times, the options should be properly merged. The processor should correctly identify existing plugins regardless of their position in the attachers array and update their configuration accordingly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
