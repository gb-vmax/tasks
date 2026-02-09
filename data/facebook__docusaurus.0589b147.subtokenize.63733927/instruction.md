# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content tokenization seems to get stuck in an infinite loop or produces incorrect output. The parser appears to be skipping over certain events incorrectly when processing nested content structures.

### Reproduction

```js
const remark = require('remark');
const parser = remark();

// Parse markdown with nested list items and code blocks
const input = `
- Item 1
  \`\`\`
  code block
  \`\`\`
- Item 2
`;

const ast = parser.parse(input);
// Parser hangs or produces malformed AST
```

### Expected behavior

The parser should correctly tokenize nested markdown structures (like list items containing code blocks) and produce a valid AST without getting stuck or skipping content.

### Additional context

This seems to affect documents with:
- Nested list items with chunk flow content
- Code blocks inside list items
- Any deeply nested content structures

The issue appears to be in the subtokenization logic where events are being processed. It's like the parser is jumping to the wrong position when handling content types.

---
Repository: /testbed
