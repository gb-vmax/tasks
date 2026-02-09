# Bug Report

### Describe the bug

I'm experiencing an issue with chunk information retrieval where the first chunk in a bundle seems to be missing from the chunk graph. When I try to access chunk metadata, the initial entry chunk is not available in the returned object.

### Reproduction

```js
// Build configuration with multiple chunks
const chunks = [entryChunk, chunk1, chunk2];

// Get chunk graph
const chunkGraph = getChunkGraph(chunks);

// First chunk is missing!
console.log(chunkGraph[entryChunk.fileName]); // undefined
```

When building a bundle with multiple chunks, the chunk graph object doesn't include the first chunk. Additionally, the keys in the returned object appear to be numeric indices instead of file names, which makes it impossible to look up chunk information by fileName.

### Expected behavior

All chunks should be included in the chunk graph, and the keys should be the fileName property from the rendered chunk info so that chunks can be looked up by their file names.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
