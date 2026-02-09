# Bug Report

### Describe the bug

I'm encountering an issue with MDX compilation where callback functions are being invoked incorrectly. It appears that when a callback is not provided (i.e., it's undefined or null), the code is attempting to call it anyway, which leads to unexpected behavior or potential runtime errors.

### Reproduction

```js
// When using MDX compiler with custom handlers
const result = compile(mdxContent, {
  // Configuration that results in undefined callback being passed
  remarkPlugins: [
    // plugin that doesn't provide a callback
  ]
});
```

The issue occurs during the compilation process when the closer function receives an undefined callback parameter but still attempts to invoke it.

### Expected behavior

When no callback is provided (undefined/null), the function should skip the callback invocation entirely and only execute the exit logic. The compiler should handle cases where callbacks are optional gracefully without attempting to call undefined functions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
