# Bug Report

### Describe the bug

I'm experiencing an issue with asset file name generation. When using the `[name]` placeholder in the asset file name pattern, the generated name is incorrect - it appears to be truncated or mangled in an unexpected way.

### Reproduction

```js
// rollup.config.js
export default {
  output: {
    assetFileNames: '[name]-[hash][extname]'
  }
}

// When emitting an asset file named 'my-asset.css'
// Expected output: my-asset-abc123.css
// Actual output: y-asset-abc123.css (first character missing)
```

The first character of the asset name seems to be getting cut off. For example:
- `styles.css` becomes `tyles-[hash].css`
- `bundle.js` becomes `undle-[hash].js`
- `image.png` becomes `mage-[hash].png`

### Expected behavior

The `[name]` placeholder should return the full base name of the asset file (filename without extension), not a truncated version.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
