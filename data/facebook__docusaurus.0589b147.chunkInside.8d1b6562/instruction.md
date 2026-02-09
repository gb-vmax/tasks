# Bug Report

### Describe the bug

I'm experiencing an infinite loop when parsing certain markdown content. The parser seems to get stuck and never completes, causing the application to hang indefinitely.

### Reproduction

```js
const remark = require('remark');

const markdown = `
Some content here
`;

// This hangs indefinitely
const result = remark().parse(markdown);
```

The issue occurs when processing markdown with specific patterns, particularly when there are line endings or null characters in the content. The parser enters an infinite recursion and never returns.

### Expected behavior

The parser should complete successfully and return the parsed AST without hanging or entering an infinite loop.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
