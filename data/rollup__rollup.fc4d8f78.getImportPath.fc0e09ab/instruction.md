# Bug Report

### Describe the bug

I'm experiencing an issue with external module imports where the import paths are being generated incorrectly. It seems like the path normalization logic is inverted - when `renormalizeRenderPath` is true, the code is returning the raw filename instead of computing the proper relative path, and vice versa.

### Reproduction

```js
// Setup external chunk with renormalizeRenderPath enabled
const externalChunk = new ExternalChunk({
  renormalizeRenderPath: true,
  format: 'amd'
});

// Try to get import path
const importPath = externalChunk.getImportPath('/src/importer.js');

// Expected: computed relative path using getImportPath()
// Actual: just returns the filename directly
```

This also affects the AMD format check - it appears to be using the wrong boolean condition.

### Expected behavior

When `renormalizeRenderPath` is enabled, the import path should be computed using `getImportPath()` with proper relative path calculation. When it's disabled, it should just return the filename directly.

The AMD format detection should also be checking for `format === 'amd'` not `format !== 'amd'`.

### System Info
- rollup version: latest
- Node version: 18.x

---
Repository: /testbed
