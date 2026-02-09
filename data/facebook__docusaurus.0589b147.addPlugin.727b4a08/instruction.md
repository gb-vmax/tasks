# Bug Report

### Describe the bug

I'm experiencing an issue with plugin configuration in MDX where plugin parameters are being applied in the wrong order when a plugin is registered multiple times with different options.

### Reproduction

```js
const processor = unified()
  .use(somePlugin, { option1: 'first' })
  .use(somePlugin, { option2: 'second' })

// The plugin receives options in unexpected order
// Expected: { option1: 'first', option2: 'second' } as primary, then rest
// Actual: options appear to be reversed or incorrectly ordered
```

### Expected behavior

When the same plugin is registered multiple times with different configuration objects, the parameters should be merged and applied in the correct order. The primary configuration object should come first in the parameters array, followed by any additional parameters.

### Additional context

This seems to affect how plugins receive their configuration when they're added to the processor multiple times. The order of parameters matters for proper plugin initialization.

---
Repository: /testbed
