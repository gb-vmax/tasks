# Bug Report

### Describe the bug

I'm experiencing an issue with asset file name generation where the filename pattern is not being rendered correctly. When using custom `assetFileNames` patterns with placeholders like `[name]` and `[hash]`, the output filenames are incorrect.

### Reproduction

```js
// rollup.config.js
export default {
  output: {
    assetFileNames: 'assets/[name]-[hash][extname]'
  }
}

// When emitting an asset file named 'style.css'
// Expected: assets/style-abc123.css
// Actual: assets/tyle-bc123.css (first character missing from name, hash truncated incorrectly)
```

The `[name]` placeholder seems to be missing the first character of the actual filename, and the `[hash]` placeholder appears to be truncated from the wrong position.

### Expected behavior

The generated asset filenames should correctly substitute the `[name]` placeholder with the full basename (without extension) and `[hash]` should use the proper portion of the source hash.

### Additional context

This appears to affect all emitted assets when using filename patterns. The issue manifests as:
- The name portion starts from index 1 instead of 0 (missing first character)
- The hash is being sliced incorrectly, always starting from position 0 with wrong size calculation

---
Repository: /testbed
