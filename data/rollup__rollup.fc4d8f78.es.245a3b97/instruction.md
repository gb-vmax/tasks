# Bug Report

### Describe the bug

When using `import.meta.ROLLUP_FILE_URL_<referenceId>` in ES module output format, the generated code produces incorrect results. The URL resolution seems to be broken - instead of getting a proper URL object or string, the output is inverted or malformed.

### Reproduction

```js
// Input code
const assetUrl = import.meta.ROLLUP_FILE_URL_0;
console.log(assetUrl);

// After bundling with format: 'es'
// The generated code doesn't resolve the URL correctly
// Expected: proper URL string or URL object
// Actual: incorrect/inverted output
```

### Steps to reproduce:
1. Reference an asset file using `import.meta.ROLLUP_FILE_URL_<referenceId>`
2. Build with output format set to `es`
3. The generated code for URL resolution is incorrect

### Expected behavior

The `import.meta.ROLLUP_FILE_URL_*` should correctly resolve to either a URL string or URL object depending on the context, similar to how it works in other output formats like `cjs` or `system`.

### Additional context

This appears to be specific to the ES module format. Other formats seem to handle the URL resolution correctly. The issue might be related to how the relative path and `import.meta.url` are being processed together.

---
Repository: /testbed
