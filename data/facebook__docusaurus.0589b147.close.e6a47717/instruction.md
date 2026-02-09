# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where closing tokens are not being processed correctly. It appears that when a token needs to be closed, the exit handler is not being called in certain cases, which causes the parser to fail or produce incorrect output.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Try parsing markdown with nested structures
const markdown = `
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result);
```

When parsing markdown with nested elements (like bold/italic text or lists), the closing logic doesn't seem to execute properly. The parser either hangs or produces malformed AST output.

### Expected behavior

The parser should correctly process all closing tokens and call the appropriate exit handlers to build a valid AST structure. Nested markdown elements should be properly closed and the resulting tree should be well-formed.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
