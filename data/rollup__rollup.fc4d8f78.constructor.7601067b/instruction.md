# Bug Report

### Describe the bug

I'm experiencing an issue with source map generation where the sources and names arrays appear to be swapped or incorrectly mapped. When I generate a bundle with source maps enabled, the resulting source map has garbled/incorrect data - the source file names seem to be appearing where variable names should be, and vice versa.

### Reproduction

```js
// Generate a bundle with source maps
const bundle = await rollup({
  input: 'src/index.js',
  plugins: [/* your plugins */]
});

const { output } = await bundle.generate({
  sourcemap: true
});

// Inspect the source map
console.log(output[0].map.sources); // Shows variable names instead of file paths
console.log(output[0].map.names);   // Shows file paths instead of variable names
```

### Expected behavior

The source map should have:
- `sources` array containing the source file paths
- `names` array containing the variable/identifier names from the original code

Instead, these two arrays seem to be switched around, making the source map unusable for debugging.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is breaking our debugging workflow as the browser dev tools can't properly map back to the original source files.

---
Repository: /testbed
