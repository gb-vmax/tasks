# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where position tracking seems to be incorrect. When parsing MDX content, the internal position indices appear to be swapped, leading to incorrect buffer and index values being reported.

### Reproduction

```js
// Parse some MDX content with the tokenizer
const result = await compile('# Hello\n\nSome content here', {
  // ... options
});

// The internal position tracking (_index and _bufferIndex) 
// are swapped in the token positions
```

When I inspect the token positions during parsing, the `_index` and `_bufferIndex` values seem to be reversed from what they should be. This affects any downstream processing that relies on accurate position information.

### Expected behavior

The `_index` and `_bufferIndex` properties should correctly reflect their respective values from the point object, not have their assignments swapped.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have appeared in the latest version. The position tracking was working correctly before.

---
Repository: /testbed
