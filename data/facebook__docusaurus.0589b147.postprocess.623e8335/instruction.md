# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser appears to hang indefinitely when processing certain content. The process becomes unresponsive and never completes, requiring a force kill.

### Reproduction

```js
const remark = require('remark');

const content = `
# Test Document

Some content here with **bold** and *italic* text.

- List item 1
- List item 2
`;

// This call never returns
const result = remark().parse(content);
console.log('This line is never reached');
```

### Expected behavior

The parser should complete processing and return the parsed AST without hanging. The parsing should finish in a reasonable amount of time.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The same code was working fine before. Any ideas what might be causing this?

---
Repository: /testbed
