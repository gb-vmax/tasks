# Bug Report

### Describe the bug

The `Parser.parse()` method is not returning the parsed result, causing it to return `undefined` instead of the expected parse tree.

### Reproduction

```js
const Parser = require('./remark-mdx');

const input = '# Hello World';
const result = Parser.parse(input, {});

console.log(result); // undefined (expected: parse tree object)
```

### Expected behavior

The `parse()` method should return the parsed AST/tree structure from the input, not `undefined`.

### Additional context

This appears to affect any code that relies on getting the parse result directly from `Parser.parse()`. The parsing might be happening internally but the result is not being returned to the caller.

---
Repository: /testbed
