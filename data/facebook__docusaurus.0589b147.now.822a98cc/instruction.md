# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in the tokenizer. When parsing MDX content, the position information (line, column, offset) seems to be returning incorrect values. The `offset` and `_bufferIndex` properties appear to be swapped, which is causing problems when trying to get accurate source locations for tokens.

### Reproduction

```js
// When tokenizing MDX content
const tokenizer = createTokenizer(parser, initialize, from);
const position = tokenizer.now();

// The position object has swapped values:
// position.offset contains what should be in _bufferIndex
// position._bufferIndex contains what should be in offset
console.log(position);
// Expected: { line: 1, column: 5, offset: 10, _index: 2, _bufferIndex: 8 }
// Actual: { line: 1, column: 5, offset: 8, _index: 2, _bufferIndex: 10 }
```

### Expected behavior

The `now()` function should return position information with correct values:
- `offset` should contain the actual offset value from `point4.offset`
- `_bufferIndex` should contain the actual buffer index value from `point4._bufferIndex`

Currently these two values are being swapped in the returned object, which breaks position tracking throughout the parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
