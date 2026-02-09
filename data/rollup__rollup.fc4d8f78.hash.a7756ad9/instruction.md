# Bug Report

### Describe the bug

The `hash` placeholder in asset file names is generating incorrect hash values. When using the `[hash]` or `[hash:size]` placeholder in the output file name pattern, the generated hash doesn't match the expected value from the asset content.

### Reproduction

```js
// rollup.config.js
export default {
  // ...
  output: {
    assetFileNames: 'assets/[name]-[hash][extname]'
  }
}
```

When building, the hash in the output filename appears to be:
- Missing the first character
- Potentially truncated incorrectly when a custom size is specified

For example, with `[hash:8]`, instead of getting the first 8 characters of the content hash, the output seems to skip the first character and then take characters from position 1 onwards.

### Expected behavior

The `[hash]` placeholder should generate a hash value that:
1. Starts from the beginning of the computed source hash
2. Respects the size parameter correctly (e.g., `[hash:8]` should give exactly the first 8 characters)
3. Defaults to the standard hash size when no size is specified

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
