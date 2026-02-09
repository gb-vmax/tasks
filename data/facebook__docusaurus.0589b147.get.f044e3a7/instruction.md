# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue when using the remark-mdx library. The application crashes with a "Maximum call stack size exceeded" error during module initialization.

### Reproduction

```js
// Simply importing the module causes the stack overflow
import remarkMdx from 'remark-mdx';

// The error occurs before any code can execute
```

The crash happens immediately when the module is loaded, before any actual MDX processing takes place.

### Expected behavior

The module should load successfully without throwing a stack overflow error. Property copying during module initialization should complete normally.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to be related to how properties are being copied internally. The error suggests some kind of circular reference during the property definition phase.

---
Repository: /testbed
