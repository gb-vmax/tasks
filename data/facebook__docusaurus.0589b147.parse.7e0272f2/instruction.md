# Bug Report

### Describe the bug

The parser is not returning the parsed result when calling `Parser.parse()`. Instead of getting the parsed output, I'm receiving a parser instance object.

### Reproduction

```js
const Parser = require('remark-mdx');

const input = '# Hello World\n\nSome content here';
const result = Parser.parse(input, {});

// Expected: parsed AST
// Actual: Parser instance instead of parsed result
console.log(result);
```

### Expected behavior

`Parser.parse()` should return the parsed AST tree, not the parser instance itself. The method should internally call `.parse()` on the created instance and return that result.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
