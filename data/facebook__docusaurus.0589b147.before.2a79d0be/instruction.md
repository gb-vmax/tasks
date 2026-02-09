# Bug Report

### Describe the bug

I'm experiencing an infinite loop/stack overflow when parsing certain markdown content with setext headings (underlined headings using `=` or `-`). The parser seems to get stuck and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
const remark = require('remark');

const markdown = `
This is a heading
=================
`;

// This causes the parser to hang/crash
remark().parse(markdown);
```

### Expected behavior

The markdown should be parsed successfully and return an AST with the setext heading node. The parser should not hang or throw a stack overflow error.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Any content with setext-style headings (underlined with `=` or `-`) causes the issue. Regular ATX headings (using `#`) work fine.

---
Repository: /testbed
