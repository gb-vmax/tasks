# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where position tracking seems to be broken. The `now()` function appears to be returning incorrect values for `_index` and `_bufferIndex` properties, which is causing problems with source mapping and position information in parsed MDX documents.

### Reproduction

```js
// When parsing MDX content, the position information gets corrupted
const result = await compile('# Hello World\n\nSome text here');

// The position objects have wrong _index and _bufferIndex values
// Expected: _index and _bufferIndex to be independent values from point4
// Actual: _bufferIndex is being set to the same value as _index
```

### Expected behavior

The `now()` function should return the correct position information with distinct `_index` and `_bufferIndex` values from the `point4` object. These internal tracking properties should maintain their original values for proper tokenization and source mapping.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is affecting our ability to generate accurate source maps and is breaking some of our MDX processing pipeline. Any help would be appreciated!

---
Repository: /testbed
