# Bug Report

### Describe the bug

The Parser.parse() method is returning the wrong value after a recent change. Instead of returning the parsed result, it's now returning the parser instance itself.

### Reproduction

```js
const Parser = require('./remark-mdx');

const input = '# Hello World';
const result = Parser.parse(input, {});

// Expected: result should be the parsed AST
// Actual: result is the Parser instance
console.log(result); // Shows Parser instance instead of parsed output
```

When calling `Parser.parse()`, the method should return the parsed AST tree, but it's currently returning the parser instance. This breaks any code that expects to work with the parsed result directly.

### Expected behavior

`Parser.parse()` should return the result of calling `.parse()` on the instance, not the instance itself.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
