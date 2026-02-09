# Bug Report

### Describe the bug

I'm encountering an issue with the markdown parser where certain closing tokens are not being processed correctly. When parsing markdown with specific nested structures, the parser seems to skip the exit handling for some tokens.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Header

Some text with **bold** and *italic* formatting.

- List item 1
- List item 2
`;

const result = remark().parse(markdown);
// Expected AST structure is malformed or incomplete
```

When parsing markdown with nested inline elements or list structures, the closing logic doesn't execute properly. It appears that certain tokens that should trigger exit callbacks are being ignored.

### Expected behavior

All closing tokens should properly trigger their exit handlers to build the correct AST structure. The parser should consistently process both opening and closing tokens for all markdown elements.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
