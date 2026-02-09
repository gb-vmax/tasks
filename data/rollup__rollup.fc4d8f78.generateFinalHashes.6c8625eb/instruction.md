# Bug Report

### Describe the bug

When building with hash placeholders in filenames, the generated hashes are not accumulating content from all dependencies. Each iteration overwrites the previous content instead of appending to it, which means the final hash only reflects the last dependency rather than all of them combined.

### Reproduction

```js
// Create a bundle with multiple chunks that have hash dependencies
// For example, chunk A imports chunk B which imports chunk C

const config = {
  output: {
    entryFileNames: '[name]-[hash].js',
    chunkFileNames: '[name]-[hash].js'
  }
}

// Build the bundle with chunks that depend on each other
// The hash generated for the entry chunk should incorporate 
// the hashes of all its dependencies, but currently only 
// reflects the last one
```

### Expected behavior

The content hash for a chunk should be calculated by accumulating the content hashes of all its dependencies. If chunk A depends on chunks B and C, the hash for A should be based on the combined content of A, B, and C - not just C alone.

### Current behavior

The hash generation loop overwrites `contentToHash` on each iteration instead of concatenating, so only the last dependency's hash is included in the final calculation. This can lead to:
- Different chunks getting the same hash when they shouldn't
- Cache invalidation not working properly when deep dependencies change
- Potential hash collisions in larger bundles

This affects builds with multiple levels of chunk dependencies where proper content-based hashing is critical for cache busting.

---
Repository: /testbed
