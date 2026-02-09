# Bug Report

### Describe the bug

I'm encountering an issue with expression statement generation where certain object expressions are not being properly wrapped in parentheses. This causes syntax errors in the generated code when object literals appear at the start of expression statements.

### Reproduction

```js
// When generating code for an expression statement with an object literal
// The output is missing parentheses, resulting in invalid syntax

// Example that triggers the issue:
const ast = {
  type: 'ExpressionStatement',
  expression: {
    type: 'ObjectExpression',
    properties: [...]
  }
}

// Generated output (incorrect):
// {foo: 'bar'};

// Expected output:
// ({foo: 'bar'});
```

### Expected behavior

Object expressions at the start of expression statements should be automatically wrapped in parentheses to prevent them from being parsed as block statements. The generator should correctly identify when parentheses are needed based on the expression type.

### Additional context

This seems to affect object expressions and possibly other expression types that need parentheses when appearing as standalone statements. The issue appears in the code generation logic for `ExpressionStatement` nodes.

---
Repository: /testbed
