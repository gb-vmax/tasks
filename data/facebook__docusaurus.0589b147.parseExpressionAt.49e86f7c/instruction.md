# Bug Report

### Describe the bug

I'm encountering an issue with expression parsing where `parseExpressionAt` seems to be skipping tokens unexpectedly. When trying to parse expressions at specific positions in the input, the parser appears to advance too far and sometimes returns `undefined` instead of the parsed expression.

### Reproduction

```js
const { parseExpressionAt } = require('@mdx-js/mdx');

// Trying to parse a simple expression at position 0
const input = 'myVariable';
const result = parseExpressionAt(input, 0);

console.log(result); // Expected: expression AST node, Actual: undefined
```

### Expected behavior

The parser should correctly parse the expression at the given position and return the corresponding AST node. It shouldn't skip over valid tokens or return undefined for valid expressions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
