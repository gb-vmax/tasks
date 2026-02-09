# Bug Report

### Describe the bug

I'm experiencing an infinite loop/hang when parsing certain markdown content. The parser seems to get stuck and never completes, causing the application to freeze.

### Reproduction

```js
// Parsing this content causes the application to hang
const markdown = `Some text content`;

const result = remark.parse(markdown);
// Never completes - application freezes here
```

The issue appears when processing text data in markdown files. The parser enters an infinite state and doesn't progress or return.

### Expected behavior

The parser should complete successfully and return the parsed AST without hanging or entering an infinite loop.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
