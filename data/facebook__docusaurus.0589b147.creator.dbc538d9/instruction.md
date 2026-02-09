# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where tokenization fails when processing certain markdown content. The parser seems to be unable to properly initialize tokenizers, causing parsing to fail silently or produce incorrect output.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Header

Some text with **bold** and *italic*.
`;

const result = remark.parse(markdown);
// Parser fails to properly tokenize the content
```

When trying to parse markdown content, the tokenizer initialization appears to be broken. The parsed output is either incomplete or doesn't match the expected AST structure.

### Expected behavior

The parser should correctly tokenize and parse markdown content, producing a valid AST that represents all elements in the input (headers, emphasis, strong text, etc.).

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have started happening recently. The parser was working fine before but now fails to process even basic markdown structures correctly.

---
Repository: /testbed
