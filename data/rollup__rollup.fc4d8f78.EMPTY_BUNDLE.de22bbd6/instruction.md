# Bug Report

### Describe the bug

The warning message for empty bundles is displaying incorrect grammar. When a single empty chunk is generated, the message shows "Generated an empty chunks" instead of "Generated an empty chunk". Similarly, when multiple empty chunks are generated, it shows "Generated empty chunk" instead of "Generated empty chunks".

### Reproduction

```js
// When building with a configuration that produces one empty chunk:
// Current output: "Generated an empty chunks"
// Expected output: "Generated an empty chunk"

// When building with a configuration that produces multiple empty chunks:
// Current output: "Generated empty chunk"  
// Expected output: "Generated empty chunks"
```

### Expected behavior

The warning message should use proper singular/plural forms:
- For 1 empty chunk: "Generated an empty chunk"
- For multiple empty chunks: "Generated empty chunks"

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
