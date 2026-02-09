# Bug Report

### Describe the bug

I'm experiencing an issue with ternary operator (conditional expression) code generation where the output is incorrect. When using nested conditional expressions, the generated code seems to be calling the wrong node type handler, resulting in malformed JavaScript output.

### Reproduction

```js
// Input AST with nested conditional expression
const ast = {
  type: 'ConditionalExpression',
  test: {
    type: 'Identifier',
    name: 'condition'
  },
  consequent: {
    type: 'Literal',
    value: 'yes'
  },
  alternate: {
    type: 'Literal', 
    value: 'no'
  }
}

// Generate code from the AST
// Expected output: condition ? "yes" : "no"
// Actual output: appears to be using wrong node type for consequent/alternate
```

### Expected behavior

The code generator should properly handle the consequent and alternate branches of conditional expressions by using their respective node types. For example, a Literal node in the consequent should be processed as a Literal, not as a ConditionalExpression.

### Additional context

This seems to affect any ternary expressions in the generated code. The issue appears to be in how the consequent and alternate branches are being processed - they should use their own node types rather than the parent ConditionalExpression type.

---
Repository: /testbed
