# Bug Report

### Describe the bug

I'm encountering an issue where chunks without hash placeholders are being added to the `nonHashedChunksWithPlaceholders` array even when they shouldn't be. This appears to be causing all transformed chunks to be treated as non-hashed chunks with placeholders, regardless of whether they actually have a `hashPlaceholder` or not.

### Reproduction

```js
// When transforming chunks during the build process
// Chunks without hashPlaceholder are incorrectly added to nonHashedChunksWithPlaceholders

const transformedChunk = {
  code: '/* some code */',
  map: null
}

// Even though hashPlaceholder is undefined/falsy, 
// the chunk still gets pushed to nonHashedChunksWithPlaceholders
```

### Expected behavior

Only chunks that actually have a `hashPlaceholder` should be added to the `nonHashedChunksWithPlaceholders` array. Chunks without hash placeholders should not be included in this array since they don't need placeholder replacement.

### Additional context

This seems to affect the content hashing logic during the chunk rendering phase. The conditional block that was supposed to separate hashed vs non-hashed chunks doesn't appear to be working correctly anymore.

---
Repository: /testbed
