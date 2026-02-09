# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the position tracking for data nodes appears to be incorrect. When parsing markdown content, the end position of text nodes is being set to the start position instead of the actual end position.

Additionally, there seems to be a problem with how elements are being removed from the processing stack - instead of removing the last element (LIFO), it's removing from the beginning (FIFO), which breaks the nested structure handling.

### Reproduction

```js
const remark = require('remark');

const markdown = `
Hello world
Some text here
`;

const ast = remark.parse(markdown);

// Check the position of text nodes
console.log(ast.children[0].children[0].position);
// Expected: end position should be after "Hello world"
// Actual: end position is at the start of the text
```

### Expected behavior

1. The `position.end` for data/text nodes should point to the actual end of the content, not the start
2. Stack operations should maintain proper LIFO order (pop from end, not shift from beginning)

This is causing issues when trying to use position information for source mapping or when processing the AST for transformations.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
