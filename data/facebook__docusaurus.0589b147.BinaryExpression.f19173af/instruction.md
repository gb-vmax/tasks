# Bug Report

### Describe the bug

I'm encountering an issue with the code generator where binary expressions are being incorrectly wrapped in parentheses. Specifically, all binary operators except "in" are now being wrapped in parentheses, when it should be the opposite - only the "in" operator should be wrapped.

### Reproduction

```js
// When generating code for a binary expression like:
const expr = {
  type: 'BinaryExpression',
  operator: '+',
  left: { type: 'Identifier', name: 'a' },
  right: { type: 'Identifier', name: 'b' }
}

// The output is: (a + b)
// But it should be: a + b

// Meanwhile, for the "in" operator:
const inExpr = {
  type: 'BinaryExpression',
  operator: 'in',
  left: { type: 'Identifier', name: 'key' },
  right: { type: 'Identifier', name: 'obj' }
}

// The output is: key in obj
// But it should be: (key in obj)
```

### Expected behavior

The "in" operator should be wrapped in parentheses to avoid precedence issues, while other binary operators should not be automatically wrapped. Also noticed that the spacing around operators seems off - there's no space before the operator in the generated output.

This is affecting code generation for MDX files and producing invalid or unexpected JavaScript output.

---
Repository: /testbed
