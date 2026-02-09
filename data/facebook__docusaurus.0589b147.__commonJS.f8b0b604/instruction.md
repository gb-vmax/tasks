# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module loading in the MDX vendor bundle. The commonJS module wrapper appears to be returning the wrong value, which causes modules to not be properly cached and reused.

### Reproduction

When importing the same module multiple times:

```js
const mdx1 = require('@mdx-js/mdx');
const mdx2 = require('@mdx-js/mdx');

// These should be the same object, but they're not
console.log(mdx1 === mdx2); // Expected: true, Actual: false
```

The module gets re-initialized on every require instead of returning the cached version. This breaks singleton patterns and causes unexpected behavior where the same module imported in different files doesn't share state.

### Expected behavior

The `__commonJS` helper should properly cache and return the module exports on subsequent calls. When a module is required multiple times, it should return the same cached exports object instead of re-executing the module initialization.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing performance issues and breaking assumptions about module caching in our build pipeline.

---
Repository: /testbed
