# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are being processed incorrectly. The parser seems to be adding results with swapped parameters, which causes the parsed output to be malformed or completely broken.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Test heading

Some paragraph text with **bold** and *italic* formatting.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result);
```

When running this code, the parsed AST structure is incorrect - nodes appear to have their construct and position information swapped or missing entirely.

### Expected behavior

The markdown should be parsed correctly with proper AST node structure. Each node should have the correct construct type and position information in the right order.

### Additional context

This seems to affect various markdown constructs including headings, emphasis, lists, etc. The parsing completes without errors but the resulting structure is unusable.

---
Repository: /testbed
