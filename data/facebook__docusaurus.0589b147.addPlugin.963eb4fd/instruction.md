# Bug Report

### Describe the bug

When registering the same plugin multiple times with different options in MDX, the plugin parameters are being applied in the wrong order. The primary configuration object ends up at the end of the parameters array instead of at the beginning where it should be.

### Reproduction

```js
const processor = unified()
  .use(somePlugin, { option1: 'value1' })
  .use(somePlugin, { option2: 'value2' })

// Expected: plugin receives [{ option1: 'value1', option2: 'value2' }, ...rest]
// Actual: plugin receives [...rest, { option1: 'value1', option2: 'value2' }]
```

### Steps to reproduce:
1. Register a plugin with initial options
2. Register the same plugin again with additional options that should be merged
3. The merged options object appears at the wrong position in the parameters array

### Expected behavior

When a plugin is registered multiple times with options, the merged primary configuration object should be the first parameter, followed by any additional parameters. The current behavior places it at the end of the array, which breaks plugins that expect configuration as the first argument.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
