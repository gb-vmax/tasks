# Bug Report

### Describe the bug

When `renormalizeRenderPath` is enabled, the import paths generated for external chunks are not being properly escaped. The `escapeId()` function is only being applied when `renormalizeRenderPath` is false, but it should be applied in both cases to ensure proper escaping of special characters in import paths.

### Reproduction

```js
// Setup with renormalizeRenderPath enabled
const options = {
  format: 'amd',
  // ... other options
};

// Create an external chunk with renormalizeRenderPath = true
const externalChunk = new ExternalChunk(/* ... */);
externalChunk.renormalizeRenderPath = true;

// Get import path
const importPath = externalChunk.getImportPath('./some/importer.js');

// Expected: escaped path using escapeId()
// Actual: unescaped filename
console.log(importPath); // Returns raw filename without escaping
```

### Expected behavior

Import paths should always be properly escaped using `escapeId()` regardless of the `renormalizeRenderPath` setting. Special characters in module names need to be escaped to prevent issues in the generated output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
