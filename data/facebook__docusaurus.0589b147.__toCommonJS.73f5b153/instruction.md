# Bug Report

### Describe the bug
After a recent update, I'm experiencing issues with module exports when using the remark-mdx parser. It seems like the `__esModule` property is not being set correctly on exported modules, which is causing problems with interop between CommonJS and ES modules.

### Reproduction
When importing modules that have been processed through the remark-mdx vendor file, the `__esModule` flag appears to be non-enumerable, which breaks compatibility with certain bundlers and module systems that check for this property.

```js
// Import a module processed by remark-mdx
import something from 'remark-mdx';

// Attempting to check module type
console.log(Object.keys(something)); // __esModule is missing from enumerable properties
```

### Expected behavior
The `__esModule` property should be enumerable so that module detection works correctly across different module systems. This is the standard behavior for transpiled ES modules.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening in a recent change. The module interop was working fine before.

---
Repository: /testbed
