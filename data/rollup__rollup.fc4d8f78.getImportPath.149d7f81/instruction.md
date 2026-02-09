# Bug Report

### Describe the bug

I'm experiencing an issue with external module import paths. When `renormalizeRenderPath` is enabled, the import paths are not being escaped correctly, and when it's disabled, the paths are not being normalized relative to the importer.

### Reproduction

```js
// When renormalizeRenderPath is true
const chunk = new ExternalChunk(/* ... with renormalizeRenderPath: true */);
const importPath = chunk.getImportPath('/some/importer/path.js');
// Returns unescaped path instead of escaped normalized path

// When renormalizeRenderPath is false  
const chunk2 = new ExternalChunk(/* ... with renormalizeRenderPath: false */);
const importPath2 = chunk2.getImportPath('/some/importer/path.js');
// Returns just the filename instead of the escaped normalized path
```

### Expected behavior

- When `renormalizeRenderPath` is `true`, it should return the escaped normalized import path
- When `renormalizeRenderPath` is `false`, it should return just the escaped filename

Currently the behavior seems inverted - the logic appears to be backwards.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
