# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where position tracking appears to be broken. When processing certain markdown content, the parser seems to be calculating incorrect offsets and buffer indices, leading to completely wrong position information in the AST nodes.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `Some **bold text** here`;
const ast = processor.parse(markdown);

// The position information for nodes is completely off
// Expected: accurate column, offset, and buffer index values
// Actual: values appear to be accumulating incorrectly
console.log(ast);
```

When parsing markdown with emphasis/attention markers (like `**bold**` or `*italic*`), the position tracking seems to compound errors. The `column`, `offset`, and `_bufferIndex` values in the position objects don't match the actual positions in the source text.

### Expected behavior

Position information should accurately reflect the actual location of nodes in the source markdown. Each point should have correct `column`, `offset`, and `_bufferIndex` values that correspond to the actual character positions.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken recently and is affecting any markdown processing that relies on accurate position information for source mapping or error reporting.

---
Repository: /testbed
