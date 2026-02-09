# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where the tree-shaking behavior seems inverted. When I access specific properties from a dynamically imported module, the bundler appears to be treating them as if I'm accessing unknown properties, and vice versa.

### Reproduction

```js
// module.js
export const foo = 'foo';
export const bar = 'bar';
export const baz = 'baz';

// main.js
import('./module.js').then(mod => {
  console.log(mod.foo); // Accessing a specific known property
});
```

When bundling this code, it seems like the bundler is incorrectly marking the import as having unknown accessed keys when I'm actually accessing a specific property (`foo`). This affects tree-shaking and causes the entire module to be included even when only specific exports are used.

### Expected behavior

When accessing a specific property from a dynamic import (like `mod.foo`), the bundler should:
1. Recognize that a known property is being accessed
2. Only include the necessary exports in the bundle
3. Properly tree-shake unused exports

Instead, it appears to be doing the opposite - treating known property accesses as unknown, which prevents proper tree-shaking optimization.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be a regression as dynamic import tree-shaking was working correctly in previous versions.

---
Repository: /testbed
