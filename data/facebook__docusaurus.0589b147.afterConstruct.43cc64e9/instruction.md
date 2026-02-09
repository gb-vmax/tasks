# Bug Report

### Describe the bug

I'm encountering an infinite loop issue when parsing markdown content that ends with a null character. The parser seems to get stuck and never completes, causing the application to hang.

### Reproduction

```js
const remark = require('remark');

// This causes an infinite loop
const content = "Some markdown text";
const result = remark.parse(content);
// Parser hangs and never returns
```

The issue appears to be related to how the flow parser handles the end of input. When the parser encounters a null character (end of file), it should properly terminate, but instead it seems to recursively call itself indefinitely.

### Expected behavior

The parser should complete successfully and return the parsed AST without hanging. Parsing should terminate cleanly when reaching the end of the input.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
