# Bug Report

### Describe the bug
When parsing markdown with blank lines at the end of flow content, the parser is producing incorrect token sequences. The `lineEndingBlank` tokens are being generated in the wrong order or at unexpected positions, which breaks the expected AST structure.

### Reproduction
```js
const remark = require('remark');

const markdown = `
Some text

`;

const result = remark.parse(markdown);
console.log(result);
```

When parsing markdown that ends with blank lines, the token stream appears to be malformed. The `lineEndingBlank` enter/exit events seem to be happening at the wrong time relative to when the code is consumed.

### Expected behavior
The parser should correctly handle blank line endings in flow content and produce the proper token sequence with `lineEndingBlank` events in the correct order. The AST structure should be consistent regardless of whether the content ends with blank lines or not.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
