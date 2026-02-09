# Bug Report

### Describe the bug

I'm experiencing an issue with asset file name generation where the `[hash]` and `[name]` placeholders are producing incorrect output. The hash appears to be missing the first character, and the name is being truncated unexpectedly.

### Reproduction

```js
// rollup.config.js
export default {
  output: {
    assetFileNames: 'assets/[name]-[hash][extname]'
  }
}

// When emitting an asset with name "style.css"
// Expected: assets/style-a1b2c3d4.css
// Actual: assets/styl-1b2c3d4e.css
```

The hash value seems to be offset by one character (missing the first character), and the filename without extension is also being cut off incorrectly.

### Expected behavior

- `[hash]` should include all characters of the hash starting from the beginning
- `[name]` should return the complete filename without the extension, not truncated

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
