# Bug Report

### Describe the bug

I'm experiencing issues with markdown parsing when using nested container elements. The parser seems to be handling flow content incorrectly, causing unexpected behavior when processing block-level elements within containers.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
> This is a blockquote
> 
> - with a list
> - inside it
`;

const result = processor.parse(markdown);
// The AST structure is malformed or throws an error
```

When parsing markdown with containers (like blockquotes) that have flow content (block elements like lists, paragraphs) nested inside them, the parser doesn't process them correctly. The issue appears to be related to how the context is being passed around during parsing.

### Expected behavior

The parser should correctly handle nested flow content within container elements and produce a valid AST. Container elements should properly process their child block-level elements.

### System Info
- remark version: 15.0.1
- Node version: Latest LTS

---
Repository: /testbed
