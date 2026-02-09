# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link/image title parsing. When processing titles in links or images, the parser seems to be producing incorrect token sequences, which is causing the AST structure to be malformed.

### Reproduction

```js
const remark = require('remark');

const markdown = `[link](url "title")`;
const ast = remark.parse(markdown);

// The token structure for the title appears incorrect
// The markerType and stringType tokens are in the wrong order
console.log(ast);
```

When parsing markdown with titles (the quoted text after URLs in links/images), the resulting AST doesn't have the proper token hierarchy. It looks like the enter/exit calls for `stringType` and `markerType` tokens are not properly nested.

### Expected behavior

The parser should generate a properly structured AST where tokens are entered and exited in the correct order. The `stringType` token should wrap the entire title string content, and `markerType` tokens should be properly nested within it.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
