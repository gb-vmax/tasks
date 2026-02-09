# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the tokenizer seems to be processing chunks in the wrong order. This causes incorrect serialization of tokens, leading to garbled or incorrect output when parsing markdown content.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello World

This is a test document with **bold text** and *italic text*.
`;

const result = remark.parse(markdown);
// The parsed output is incorrect - tokens appear to be in wrong order
```

When I parse markdown documents, the resulting AST has tokens that don't match the expected structure. It seems like the chunks are being passed in the wrong order during the slicing operation.

### Expected behavior

The markdown parser should correctly tokenize and serialize the input, producing a valid AST with tokens in the proper order matching the source document structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
