# Bug Report

### Describe the bug

When using asset file name patterns with the `[name]` placeholder, the generated file names are incorrect. The extension is being included in the name portion instead of being properly stripped out.

### Reproduction

```js
// rollup.config.js
export default {
  output: {
    assetFileNames: 'assets/[name]-[hash][extname]'
  }
}

// When emitting an asset like "image.png"
// Expected: assets/image-abc123.png
// Actual: assets/image.pngpng-abc123.png or similar incorrect output
```

The `[name]` placeholder should return just the filename without the extension, but it appears to be including the extension or duplicating it somehow.

### Expected behavior

The `[name]` placeholder in `assetFileNames` should return only the base filename without the extension. For example, if the original file is `logo.png`, `[name]` should resolve to `logo`, not `logo.png` or something else.

### Additional context

This seems to have started happening recently. The hash placeholder also appears to be affected - it's returning an empty string or incorrect hash length in some cases.

---
Repository: /testbed
