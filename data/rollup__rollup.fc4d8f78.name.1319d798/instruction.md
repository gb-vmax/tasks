# Bug Report

### Describe the bug

I'm experiencing an issue with chunk naming in the build output. When generating chunks, the filename patterns are not being replaced correctly - instead of getting the actual chunk name, I'm seeing what looks like a function definition in the output path.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    dir: 'dist',
    entryFileNames: '[name]-[hash].js',
    chunkFileNames: '[name]-[hash].js'
  }
}
```

When building, the output filenames contain the string representation of a function instead of the actual chunk name.

### Expected behavior

The `[name]` placeholder in the output filename pattern should be replaced with the actual chunk name (e.g., `main-abc123.js`), not with a function's string representation.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
