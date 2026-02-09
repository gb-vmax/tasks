# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the tokenizer seems to be producing incorrect output. The parsed content doesn't match what's expected, and it appears that the token slicing mechanism is broken.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading
Some text here
`;

const result = processor.parse(markdown);
// The parsed AST is malformed or incomplete
```

When parsing markdown content, the resulting AST structure is incorrect. It seems like the tokenizer is not properly slicing the input stream, which leads to missing or corrupted nodes in the syntax tree.

### Expected behavior

The markdown parser should correctly tokenize and parse the input, producing a valid AST that accurately represents the document structure. Token positions and content should be properly extracted from the input stream.

### Additional context

This seems to affect any markdown content being parsed. The issue appears to be in the tokenization layer where input chunks are being processed. I noticed this started happening recently, possibly after an internal change to the tokenizer implementation.

---
Repository: /testbed
