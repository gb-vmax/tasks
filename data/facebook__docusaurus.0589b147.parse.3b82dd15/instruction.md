# Bug Report

### Describe the bug

The `Parser.parse()` method is not returning the parsed result. When calling `Parser.parse(input, options)`, the function returns `undefined` instead of the expected parse tree/AST.

### Reproduction

```js
const Parser = require('@mdx-js/mdx');

const input = '# Hello World';
const result = Parser.parse(input, {});

console.log(result); // undefined (expected: parsed AST object)
```

### Expected behavior

The `Parser.parse()` method should return the parsed AST/result from the `.parse()` call, not `undefined`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
