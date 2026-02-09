# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where links are not being recognized correctly. When I try to parse markdown text containing links, the parser seems to be failing silently and the links are not being converted to the expected AST nodes.

### Reproduction

```js
const remark = require('remark');
const parse = remark().parse;

const markdown = '[example link](https://example.com)';
const ast = parse(markdown);

// Expected: AST with link node
// Actual: Link is not parsed correctly
console.log(ast);
```

The same issue occurs with reference-style links:

```js
const markdown = '[example][ref]\n\n[ref]: https://example.com';
const ast = parse(markdown);
// Link reference is not being resolved
```

### Expected behavior

Links should be properly parsed into link nodes in the AST. Both inline links `[text](url)` and reference-style links `[text][ref]` should work correctly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Previously, link parsing was working fine for both inline and reference-style links.

---
Repository: /testbed
