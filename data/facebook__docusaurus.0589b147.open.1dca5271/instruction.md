# Bug Report

### Describe the bug
I'm experiencing an issue with markdown parsing where certain nested structures are not being rendered correctly. It seems like the opening/closing of tokens is happening in the wrong order, causing the parser to lose track of the node hierarchy.

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

When parsing markdown with nested inline elements (like bold text inside list items, or links with emphasis), the resulting AST structure is malformed. The parent-child relationships between nodes don't match what's expected.

### Expected behavior
The parser should correctly maintain the node hierarchy and produce a valid AST where:
- Parent nodes are entered before their children
- Child nodes are properly nested within their parents
- The token processing order matches the document structure

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently. The AST structure was working fine in earlier versions.

---
Repository: /testbed
