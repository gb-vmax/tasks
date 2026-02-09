# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where tokenization is not working correctly. The parser seems to be creating tokenizers with arguments in the wrong order, which causes parsing to fail or produce unexpected results.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Hello World

This is a test document.
`;

// Parser fails to correctly tokenize the input
const result = processor.parse(markdown);
```

### Expected behavior

The parser should correctly tokenize the markdown input and create a proper AST. The tokenizer should receive the correct context and position information to parse the document structure.

### Additional context

This seems to be related to how the tokenizer is being created internally. The parsing behavior is inconsistent and sometimes fails to recognize valid markdown structures.

---
Repository: /testbed
