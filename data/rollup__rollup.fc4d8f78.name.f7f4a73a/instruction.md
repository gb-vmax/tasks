# Bug Report

### Describe the bug

I'm experiencing an issue with filename patterns when using the `[name]` placeholder in output configuration. The chunk name is not being resolved correctly, and it seems like the context (`this`) is lost when the name function is called.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    entryFileNames: '[name]-[hash].js',
    chunkFileNames: '[name]-[hash].js'
  }
}
```

When bundling, the `[name]` placeholder doesn't expand to the actual chunk name. Instead, it either throws an error about `this` being undefined or produces an incorrect filename.

### Expected behavior

The `[name]` placeholder should be replaced with the actual chunk name, just like it worked in previous versions. The filename should be something like `main-abc123.js` instead of failing or producing malformed names.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
