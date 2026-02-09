# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where nested structures are not being handled correctly. It seems like the order of operations when opening new nodes is causing problems with the AST structure.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some text with **bold** content.

- List item 1
- List item 2
`;

const ast = processor.parse(markdown);
// The AST structure appears malformed for nested elements
```

When processing markdown with nested inline elements (like bold text inside paragraphs, or complex list structures), the resulting AST doesn't match the expected hierarchy. Parent-child relationships seem to be inverted or incorrectly established.

### Expected behavior

The AST should correctly represent the hierarchical structure of the markdown, with proper parent-child relationships between nodes. Nested elements should be children of their containing elements, not the other way around.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
