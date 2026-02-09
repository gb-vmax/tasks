# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to hang or enter an infinite loop when processing certain markdown content. The application becomes unresponsive and never completes the parsing operation.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test Document

Some content here with **bold** and *italic* text.

- List item 1
- List item 2
`;

// This hangs indefinitely
const result = remark().parse(markdown);
console.log(result); // Never reaches here
```

### Expected behavior

The parser should complete processing and return the AST without hanging. Previously this was working fine but after a recent update the parser no longer completes.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
