# Bug Report

### Describe the bug

I'm encountering an issue with asset file name generation when using the `hash` placeholder in the output file name pattern. The generated hash appears to be incorrect - it seems to be missing the first character and the length doesn't match what I specified.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    assetFileNames: 'assets/[name]-[hash:8][extname]'
  }
}
```

When I build with this configuration, the hash in the output filename doesn't look right. For example, if the source hash should be `a1b2c3d4e5f6`, I'm getting something like `b2c3d4e5` instead of `a1b2c3d4` when requesting 8 characters.

### Expected behavior

The hash placeholder should:
1. Start from the beginning of the source hash
2. Return the correct number of characters as specified (e.g., `[hash:8]` should return 8 characters)

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started recently. The generated hashes don't match what they used to be, which is breaking my cache-busting strategy.

---
Repository: /testbed
