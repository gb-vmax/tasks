# Bug Report

### Describe the bug

The code generator is skipping the first statement in Program nodes and incorrectly increasing indentation levels for subsequent statements. When generating code from an AST, the first statement in a program body is completely omitted from the output, and each following statement gets progressively more indented.

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
};

// Generate code from this AST
// Expected output:
// 'first';
// 'second';
// 'third';

// Actual output:
// 'second';
//   'third';
// (first statement missing, third statement indented)
```

### Expected behavior

All statements in the program body should be included in the generated output with consistent indentation at the same level.

### Additional context

This appears to affect any Program node with multiple statements. The loop starts at index 1 instead of 0, causing the first statement to be skipped. Additionally, the indentation level increments inside the loop, causing each statement to be more indented than the previous one.

---
Repository: /testbed
