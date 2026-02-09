# Bug Report

### Describe the bug

I'm experiencing an issue with file name handling in the bundle output. When emitting files with different casing (e.g., `MyFile.js` vs `myfile.js`), the bundler is not properly reserving file names and seems to be overwriting entries in the bundle object.

### Reproduction

```js
// Emit a file with mixed case
this.emitFile({
  type: 'asset',
  fileName: 'MyAsset.js',
  source: 'content1'
});

// Try to emit another file with different casing
this.emitFile({
  type: 'asset', 
  fileName: 'myasset.js',
  source: 'content2'
});
```

### Expected behavior

The bundler should detect that these file names conflict (case-insensitive) and either:
1. Show a warning about the file name conflict
2. Properly reserve both file name entries in the bundle

Instead, it seems like the warning is not being shown when it should be, and the file entries are being stored incorrectly in the bundle object.

### System Info

- Rollup version: latest
- OS: macOS (case-insensitive filesystem)

This is particularly problematic on case-insensitive file systems where `MyAsset.js` and `myasset.js` would refer to the same file.

---
Repository: /testbed
