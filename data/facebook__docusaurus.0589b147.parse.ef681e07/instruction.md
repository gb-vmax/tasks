# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where tokenizer creation seems to be broken. When parsing markdown content, the parser fails to properly initialize tokenizers, which causes parsing to fail or produce incorrect results.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello World

This is a test document with some **bold** text.
`;

const result = remark.parse(markdown);
// Parser fails to correctly tokenize the content
```

### Expected behavior

The parser should correctly tokenize and parse the markdown content, creating proper AST nodes for headings, paragraphs, and inline formatting.

### Additional context

This appears to affect all markdown parsing operations. The tokenizer initialization seems to be receiving incorrect parameters, which breaks the entire parsing pipeline.

---
Repository: /testbed
