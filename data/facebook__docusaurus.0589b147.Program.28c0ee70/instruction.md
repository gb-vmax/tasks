# Bug Report

### Describe the bug

I'm encountering an issue where the first statement in a Program node is being skipped during code generation. When processing AST nodes, the generator appears to be missing the initial statement in the body array.

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
    },
    {
      type: 'ExpressionStatement',
      expression: { type: 'Literal', value: 'third' }
    }
  ]
}

// Generate code from the AST
// Expected: All three statements should be in the output
// Actual: Only 'second' and 'third' appear, 'first' is missing
```

### Expected behavior

All statements in the Program body should be processed and included in the generated output. The first statement should not be skipped.

### Additional context

This seems to affect any Program node with multiple statements. Single-statement programs work fine, but as soon as there are 2+ statements, the first one disappears from the generated code.

---
Repository: /testbed
