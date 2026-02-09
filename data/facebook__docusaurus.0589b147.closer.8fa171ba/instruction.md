# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain markdown structures are not being processed correctly. It seems like the parser is not properly closing tokens, which causes the resulting AST to be incomplete or malformed.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = processor.parse(markdown);
console.log(result);
```

When parsing markdown with nested structures (like lists with formatting, or code blocks inside lists), the output AST appears to be missing closing nodes or has an incorrect structure. The parser seems to stop processing certain elements prematurely.

### Expected behavior

The parser should correctly close all opened tokens and produce a complete, well-formed AST that represents the entire markdown structure. All nested elements should be properly represented in the tree.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
