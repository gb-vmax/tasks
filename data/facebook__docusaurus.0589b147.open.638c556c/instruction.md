# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the document structure gets completely corrupted. When parsing markdown content, the resulting AST seems to have incorrect parent-child relationships and nodes are not being properly entered into the tree.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some paragraph text.

- List item 1
- List item 2
`;

const result = processor.parse(markdown);
console.log(result);
```

When I run this, the output tree structure is malformed - nodes that should be children of certain elements are either missing or attached to the wrong parents. The hierarchy doesn't match what I'd expect from the markdown input.

### Expected behavior

The parser should create a proper AST with correct parent-child relationships. For example:
- The heading should be a direct child of the root
- Paragraphs should be properly nested
- List items should be children of the list node

Instead, the tree structure appears broken and doesn't represent the markdown correctly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently. Any help would be appreciated!

---
Repository: /testbed
