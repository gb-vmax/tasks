# Bug Report

### Describe the bug

I'm encountering an issue where chunk hashing doesn't work correctly when generating bundles. It seems like the hash placeholders in rendered chunks are not being properly resolved, resulting in incorrect or missing hash values in the final output filenames.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: {
    dir: 'dist',
    format: 'es',
    entryFileNames: '[name]-[hash].js',
    chunkFileNames: '[name]-[hash].js'
  }
}
```

When building with this configuration, the hash placeholders appear to not be replaced correctly. The chunks are rendered before the hash dependencies are properly set up, causing the hashing mechanism to fail.

### Expected behavior

The output files should have proper hash values in their filenames based on their content, like `main-a1b2c3d4.js`. The hash should be computed after chunks are rendered and all dependencies are known.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to be a regression - the build was working fine before but now the hash generation is broken.

---
Repository: /testbed
