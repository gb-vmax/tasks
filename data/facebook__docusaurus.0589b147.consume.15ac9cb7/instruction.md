# Bug Report

### Describe the bug

After a recent update, markdown parsing appears to be broken for certain content. The parser seems to be skipping characters or not advancing through the input correctly, resulting in malformed output or incomplete parsing.

### Reproduction

```js
// Parsing markdown with specific character sequences fails
const markdown = `
# Heading
Some text with special characters
- List item 1
- List item 2
`;

const result = remark.parse(markdown);
// Output is incomplete or malformed
```

### Expected behavior

The markdown parser should correctly process all input characters and advance through the buffer properly, producing complete and accurate AST output for all markdown content.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to be affecting character offset tracking and buffer position management during tokenization. The parser appears to lose track of its position in some cases.

---
Repository: /testbed
