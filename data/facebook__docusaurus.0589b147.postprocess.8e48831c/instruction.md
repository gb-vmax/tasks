# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser appears to hang or return `null` instead of properly processing the markdown content. After parsing markdown text, I either get `null` returned or the function seems to loop indefinitely without completing.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello World

This is a test document with some **bold** text.
`;

const result = remark().parse(markdown);
console.log(result); // Expected: AST object, Actual: null or hangs
```

### Expected behavior

The parser should return a valid AST (Abstract Syntax Tree) object representing the parsed markdown structure. The parsing should complete in a reasonable amount of time without hanging.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
