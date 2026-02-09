# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where phrasing content (inline elements like text, emphasis, links, etc.) inside container elements is not being handled correctly. The parsed output structure appears to be malformed or missing expected nodes.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
**Bold text** with some [link](https://example.com) inside.
`;

const ast = processor.parse(markdown);
console.log(JSON.stringify(ast, null, 2));
```

When parsing markdown with inline/phrasing elements, the resulting AST doesn't match the expected structure. The parent-child relationships seem incorrect.

### Expected behavior

The parser should correctly process phrasing content within container elements and produce a properly structured AST with correct parent-child relationships.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
