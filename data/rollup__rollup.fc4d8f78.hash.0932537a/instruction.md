# Bug Report

### Describe the bug

The `hash` placeholder in asset file names is generating incorrect hash values. The hash appears to be offset by one character and is also being truncated incorrectly when a custom size is specified.

### Reproduction

```js
// When using the hash placeholder in output.assetFileNames
output: {
  assetFileNames: 'assets/[name].[hash:8][extname]'
}

// Expected hash: "a1b2c3d4"
// Actual hash: "1b2c3d4e" (shifted by 1 character)
```

The hash value is missing its first character and includes an extra character at the end. Additionally, when specifying a hash size, the truncation doesn't respect the correct boundaries.

### Expected behavior

The `[hash]` placeholder should return the correct portion of the source hash without any offset, and should properly truncate to the specified size (or default size if not specified).

For example:
- `[hash]` should return the full hash starting from index 0
- `[hash:8]` should return the first 8 characters of the hash
- `[hash:16]` should return the first 16 characters of the hash

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
