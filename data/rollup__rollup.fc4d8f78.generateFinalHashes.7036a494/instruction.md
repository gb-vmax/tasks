# Bug Report

### Describe the bug

I'm experiencing an issue with hash generation for output files. When using content hashing in the filename pattern, the generated hash appears to be one character shorter than the placeholder length specified in the pattern.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    dir: 'dist',
    entryFileNames: '[name]-[hash:8].js',
    chunkFileNames: '[name]-[hash:8].js'
  }
}
```

After building, the output files have hashes that are only 7 characters long instead of the expected 8 characters:

```
Expected: main-a1b2c3d4.js
Actual:   main-a1b2c3d.js
```

### Expected behavior

The hash in the output filename should match the length specified in the placeholder (e.g., `[hash:8]` should produce an 8-character hash, not 7).

### Additional context

This seems to affect all hash-based filename patterns. The hash length is consistently one character shorter than what's specified in the configuration.

---
Repository: /testbed
