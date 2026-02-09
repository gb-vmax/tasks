# Bug Report

### Describe the bug

The `in` operator in binary expressions is not being wrapped in parentheses correctly. When generating code with the `in` operator, the output is missing the necessary parentheses that should surround the expression.

### Reproduction

```js
// When processing a binary expression with the 'in' operator
const ast = {
  type: 'BinaryExpression',
  operator: 'in',
  left: { /* ... */ },
  right: { /* ... */ }
}

// The generated output should be: (key in object)
// But instead it generates: key in object
```

### Expected behavior

Binary expressions using the `in` operator should be wrapped in parentheses to ensure correct precedence and avoid syntax errors in certain contexts. For example:

```js
// Expected output:
(prop in obj)

// Current (incorrect) output:
prop in obj
```

This is particularly important when the `in` expression is used in contexts where parentheses are required, such as in certain conditional statements or as part of larger expressions.

### System Info
- Version: 3.0.0
- Component: BinaryExpression generator

---
Repository: /testbed
