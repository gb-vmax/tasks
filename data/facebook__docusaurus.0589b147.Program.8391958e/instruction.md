# Bug Report

### Describe the bug

I'm experiencing an issue where the first statement in a Program node is being skipped during code generation. When processing AST nodes, the generator appears to start iterating from index 1 instead of index 0, which causes the first statement in the body to be completely omitted from the output.

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

// Generate code from the AST
const result = generate(ast);

// Expected: Both statements should be in the output
// Actual: Only the second statement appears, first one is missing
```

### Expected behavior

All statements in the Program body should be included in the generated output, starting from the first statement at index 0.

### Additional context

This seems to have started happening recently. The code generation is working fine for all other statement types, but specifically for Program nodes, the first element of the body array is being ignored.

---
Repository: /testbed
