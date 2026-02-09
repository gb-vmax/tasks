# Bug Report

### Describe the bug

I'm encountering an issue with the remark parser where it appears to be incorrectly handling the tokenizer initialization. When parsing markdown content, the parser seems to be passing arguments in the wrong order to `createTokenizer`, which is causing unexpected behavior during text processing.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Try to parse some markdown text
const result = processor.parse('# Hello World\n\nSome text here.');

// The tokenizer receives arguments in incorrect order
// Expected: createTokenizer(parser, initial, from)
// Actual: createTokenizer(parser, from, initial)
```

### Expected behavior

The `createTokenizer` function should receive its parameters in the correct order: `parser`, `initial`, and `from`. Currently it seems like `from` and `initial` are being swapped, which breaks the tokenization process.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have been introduced recently and is affecting markdown parsing reliability. Any help would be appreciated!

---
Repository: /testbed
