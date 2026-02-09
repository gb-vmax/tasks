# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions in the MDX code generator. When generating code for binary expressions (like `a + b`, `x < y`, etc.), the operands are appearing in reversed order in the output.

### Reproduction

```js
// Input AST for: a + b
const binaryExpr = {
  type: 'BinaryExpression',
  operator: '+',
  left: { type: 'Identifier', name: 'a' },
  right: { type: 'Identifier', name: 'b' }
}

// Generated output is: b + a (reversed!)
// Expected output: a + b
```

Similarly, for comparison operators:
```js
// Input: x < y
// Generated output: y < x
// Expected: x < y
```

### Expected behavior

Binary expressions should maintain the correct order of operands. The left operand should appear on the left side of the operator, and the right operand should appear on the right side.

Also noticed that the parentheses wrapping seems inverted - expressions that shouldn't have parentheses are getting wrapped, while `in` operator expressions that should be wrapped are not.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
