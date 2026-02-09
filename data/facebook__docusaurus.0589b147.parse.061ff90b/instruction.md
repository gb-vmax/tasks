# Bug Report

### Describe the bug
The parser is returning the wrong value after calling `parse()`. Instead of returning the parsed result, it's now returning the parser instance itself.

### Reproduction
```js
const Parser = require('./remark-mdx');

const input = '# Hello World';
const result = Parser.parse(input, {});

// Expected: parsed AST object
// Actual: Parser instance
console.log(result); // Shows Parser object instead of parsed content
```

### Expected behavior
`Parser.parse()` should return the parsed AST/result, not the parser instance. This breaks existing code that expects the parsed output directly.

### Additional context
This appears to have started happening recently. Code that was working before now fails because it tries to access properties on what should be the parsed result but is instead getting the parser object.

---
Repository: /testbed
