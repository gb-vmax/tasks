# Bug Report

### Describe the bug
The code generator is skipping the first statement in Program nodes. When generating code from an AST, the first statement in the program body is not being written to the output, resulting in incomplete or broken code generation.

### Reproduction
```js
const ast = {
  type: 'Program',
  body: [
    {
      type: 'ExpressionStatement',
      expression: { type: 'Literal', value: 'first' }
    },
    {
      type: 'ExpressionStatement', 
      expression: { type: 'Literal', value: 'second' }
    }
  ]
};

// Generate code from this AST
// Expected: both statements should be in the output
// Actual: only the second statement appears
```

### Expected behavior
All statements in the Program body should be included in the generated output. The first statement should not be skipped.

### System Info
- Package: @mdx-js/mdx
- Version: 3.0.0

---
Repository: /testbed
