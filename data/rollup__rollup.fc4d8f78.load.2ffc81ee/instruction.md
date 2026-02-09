# Bug Report

### Describe the bug

I'm experiencing an issue with the stdin plugin where module resolution is not working correctly. When trying to load stdin with a suffix/extension, the plugin fails to properly match the module ID.

### Reproduction

```js
// Try to load stdin with a file extension
import content from '-:.js';

// The module is not being resolved correctly
// Expected: stdin content should be loaded
// Actual: Module not found or incorrect behavior
```

The problem occurs when using stdin input with a suffix. The module ID matching logic seems to be reversed - it's checking if `stdinName` starts with the ID instead of checking if the ID starts with `stdinName`.

### Steps to reproduce:
1. Set up a rollup configuration with the stdin plugin
2. Try to import from stdin with a suffix like `-.js` or `-.ts`
3. The module fails to load properly

### Expected behavior

The stdin plugin should correctly match and load modules when the ID is `stdinName` or starts with `stdinName` followed by a dot and extension. The cached `stdinResult` should be reused instead of calling `readStdin()` multiple times.

### Environment
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
