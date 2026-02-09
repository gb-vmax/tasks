# Bug Report

### Describe the bug
The `Parser.parse()` method is returning the parser instance instead of the parsed result. This breaks any code that expects `parse()` to return the actual parsed output.

### Reproduction
```js
const Parser = require('@mdx-js/mdx');

const input = '# Hello World';
const result = Parser.parse(input, {});

// Expected: result should be the parsed AST
// Actual: result is the parser instance itself
console.log(result); // Returns parser object instead of parse result
```

### Expected behavior
The `parse()` method should return the parsed AST/result, not the parser instance. This is breaking existing code that relies on getting the parse result directly.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
