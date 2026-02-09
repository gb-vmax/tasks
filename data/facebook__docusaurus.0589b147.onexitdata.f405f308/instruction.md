# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the position information for text nodes appears to be incorrect. When parsing markdown content, the end position of data/text tokens is pointing to the start position instead of the actual end position.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = 'Hello world';
const ast = processor.parse(markdown);

// The text node's position.end should point to the end of "Hello world"
// but it's pointing to the beginning instead
console.log(ast.children[0].children[0].position);
// Expected: { start: { line: 1, column: 1, offset: 0 }, end: { line: 1, column: 12, offset: 11 } }
// Actual: { start: { line: 1, column: 1, offset: 0 }, end: { line: 1, column: 1, offset: 0 } }
```

This makes it impossible to correctly map source positions for text content in the markdown, which breaks tooling that relies on accurate position information (like linters, formatters, or syntax highlighters).

### Expected behavior

The `position.end` property of text/data nodes should correctly point to the end of the text content, not the start.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
