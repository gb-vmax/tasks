# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the position information for AST nodes is incorrect. When parsing markdown content, the end position of nodes is being set to the start position instead of the actual end position.

### Reproduction

```js
const remark = require('remark');
const parse = remark().parse;

const markdown = `# Hello World

This is a paragraph.`;

const ast = parse(markdown);

// Check the position of the heading node
console.log(ast.children[0].position);
// Expected: end position should be after "Hello World"
// Actual: end position equals start position
```

### Expected behavior

The `position.end` property of AST nodes should point to the actual end location of the node in the source text. Currently, it appears to be pointing to the start location instead, which breaks any tooling that relies on accurate source position information (like syntax highlighters, linters, or code editors).

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
