# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in the markdown tokenizer. When parsing markdown content, the internal position state appears to be incorrectly swapped, causing `_index` and `_bufferIndex` to have each other's values.

### Reproduction

```js
const parser = createTokenizer(/* ... */);

// Parse some markdown content
const result = parser.parse('# Hello World');

// Check the position information
const position = result.now();

// position._index contains the value that should be in _bufferIndex
// position._bufferIndex contains the value that should be in _index
```

### Expected behavior

The `_index` and `_bufferIndex` properties should contain their correct respective values when retrieving the current position during tokenization. The internal state tracking should maintain the proper assignment of these buffer position indicators.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
