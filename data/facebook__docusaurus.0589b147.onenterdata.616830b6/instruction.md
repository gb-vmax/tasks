# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where text nodes are being incorrectly positioned in the AST. When parsing markdown content, the text seems to be attached to the wrong parent node or sibling position.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some text here
`;

const ast = processor.parse(markdown);
console.log(ast);
```

When inspecting the AST, text nodes appear to be off by one position - they're not being added to the correct parent or sibling in the tree structure. This causes the parsed content to be malformed.

### Expected behavior

Text nodes should be correctly positioned in the AST tree, attached to their proper parent nodes at the correct sibling index. The parsed markdown structure should accurately reflect the document hierarchy.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
