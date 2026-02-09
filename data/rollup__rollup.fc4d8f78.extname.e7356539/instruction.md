# Bug Report

### Describe the bug

I'm experiencing an issue with asset file naming when using the `output.assetFileNames` option. The `[extname]` placeholder is returning an incorrect file extension - it seems to be cutting off the last character of the extension.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    assetFileNames: 'assets/[name][extname]'
  }
}
```

When building with an asset like `image.png`, the output filename becomes something like `assets/image.pn` instead of `assets/image.png`. The last character of the extension is being truncated.

### Expected behavior

The `[extname]` placeholder should return the complete file extension including the dot (e.g., `.png`, `.css`, `.jpg`). The generated asset filenames should preserve the full extension.

### Additional context

This appears to affect all asset types - I've noticed it with `.png`, `.svg`, `.css`, and `.woff` files. The `[ext]` placeholder (without the 'name' part) seems to work correctly, but `[extname]` is broken.

---
Repository: /testbed
