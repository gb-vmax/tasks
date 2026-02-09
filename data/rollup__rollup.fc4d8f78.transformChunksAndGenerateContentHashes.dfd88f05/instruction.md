# Bug Report

### Describe the bug

I'm experiencing an issue with content hashing for chunks when using hash placeholders. It appears that chunks with hash placeholders are being duplicated in the processing pipeline, which is causing unexpected behavior in the build output.

### Reproduction

```js
// Build configuration with hash placeholders enabled
export default {
  output: {
    entryFileNames: '[name]-[hash].js',
    chunkFileNames: '[name]-[hash].js'
  }
}
```

When building with the above configuration:
1. Create a project with code splitting enabled
2. Enable hash placeholders in filenames
3. Run the build process
4. The chunks with hash placeholders appear to be processed twice

### Expected behavior

Chunks with hash placeholders should only be added to the `nonHashedChunksWithPlaceholders` array once during the transformation process. Currently, they seem to be added regardless of whether the hash placeholder exists or not, leading to duplicates.

### Additional context

This seems to affect the content hash generation workflow. The chunks that have hash placeholders are being included in the non-hashed chunks collection even after their hashes are computed and stored.

---
Repository: /testbed
