# Bug Report

### Describe the bug

I'm experiencing an issue where placeholder replacement in generated chunks is not working correctly. When there are hash placeholders that need to be replaced in the output code, they remain unreplaced in the final bundle.

### Reproduction

```js
// Generate a bundle with hash placeholders
const bundle = await rollup({
  input: 'src/index.js',
  output: {
    file: 'dist/bundle-[hash].js',
    format: 'es'
  }
});

// The output file should have the hash replaced
// but the placeholders remain as-is: bundle-[hash].js
```

### Expected behavior

When hash placeholders exist in the output configuration, they should be replaced with actual hash values in both the filename and the code content. Currently it seems like the replacement logic is inverted - placeholders are only being replaced when there are NO hashes to replace, which doesn't make sense.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues in production builds where we rely on content hashing for cache busting. The generated files still contain the literal `[hash]` placeholder text instead of the computed hash values.

---
Repository: /testbed
