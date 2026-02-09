# Bug Report

### Describe the bug

I'm experiencing an issue with external chunk import paths in my build output. When `renormalizeRenderPath` is enabled, the generated import paths appear to be incorrect - they're using the raw file name instead of the properly normalized relative path from the importer.

### Reproduction

```js
// Setup with renormalizeRenderPath enabled
const externalChunk = new ExternalChunk({
  renormalizeRenderPath: true,
  format: 'amd'
});

// When getting the import path
const importPath = externalChunk.getImportPath('/src/main.js');

// Expected: relative path from importer to chunk
// Actual: just the chunk filename without normalization
```

### Expected behavior

When `renormalizeRenderPath` is `true`, the import path should be calculated relative to the importer using `getImportPath()`. When it's `false`, it should just return the filename directly.

Currently it seems like the behavior is inverted - files are not being renormalized when they should be.

### System Info
- rollup version: latest
- Node version: 18.x

---
Repository: /testbed
