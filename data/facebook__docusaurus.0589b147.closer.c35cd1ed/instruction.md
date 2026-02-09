# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain content is not being processed correctly. It seems like the parser is skipping or not properly closing some elements, which results in malformed output.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some **bold text** and *italic text*.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result);
```

When running this code, the output is incomplete or missing expected closing tags/nodes. The AST structure appears to be malformed with some nodes not being properly closed.

### Expected behavior

The markdown should be fully parsed with all elements properly opened and closed. The resulting AST should have a complete tree structure with all nodes correctly nested and terminated.

### Additional context

This seems to have started happening recently. The parser appears to be exiting early or not processing certain token closures. Nested elements (like bold/italic text within lists) are particularly affected.

---
Repository: /testbed
