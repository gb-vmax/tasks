# Bug Report

### Describe the bug

I'm experiencing an issue where chunk name placeholders are not being resolved correctly in the output file names. The `[name]` placeholder in the output pattern seems to be broken and doesn't get replaced with the actual chunk name.

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

When building, the `[name]` placeholder doesn't get substituted properly. The output files either have incorrect names or the build fails depending on the configuration.

### Expected behavior

The `[name]` placeholder should be replaced with the actual chunk name (e.g., the entry point name or the dynamically imported module name). For example, if my entry is `index.js`, the output should be something like `index-a1b2c3d4.js`.

### System Info

- Rollup version: latest
- Node version: 18.x

This wasn't happening in previous versions, so it might be a recent regression. Any help would be appreciated!

---
Repository: /testbed
