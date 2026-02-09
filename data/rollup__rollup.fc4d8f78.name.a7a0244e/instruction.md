# Bug Report

### Describe the bug

I'm experiencing an issue with asset file naming where the `[name]` placeholder in the output file pattern is being replaced with an empty string instead of the actual filename (without extension).

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    assetFileNames: 'assets/[name]-[hash][extname]'
  },
  plugins: [
    // ... plugins that emit assets
  ]
}
```

When emitting an asset file like `logo.png`, I expect the output to be something like `assets/logo-abc123.png`, but instead I'm getting `assets/-abc123.png` (the name part is completely missing).

### Expected behavior

The `[name]` placeholder should be replaced with the filename without its extension. For example:
- Input: `logo.png` → Expected output: `assets/logo-abc123.png`
- Input: `styles.css` → Expected output: `assets/styles-def456.css`

Currently, the name portion is always empty regardless of the input filename.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
