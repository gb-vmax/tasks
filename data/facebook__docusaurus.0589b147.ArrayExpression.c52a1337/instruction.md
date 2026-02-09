# Bug Report

### Describe the bug

I'm encountering an issue with array expression generation where the first element of arrays is being skipped. When generating code from an AST, arrays are missing their first element in the output.

### Reproduction

```js
// Input AST representing: [1, 2, 3]
const arrayNode = {
  type: 'ArrayExpression',
  elements: [
    { type: 'Literal', value: 1 },
    { type: 'Literal', value: 2 },
    { type: 'Literal', value: 3 }
  ]
};

// Expected output: [1, 2, 3]
// Actual output: [2, 3]
```

The generated code is missing the first element. It seems like the array iteration is starting from index 1 instead of 0.

### Expected behavior

All array elements should be included in the generated output. An array `[1, 2, 3]` should generate the code `[1, 2, 3]`, not `[2, 3]`.

### Additional context

This appears to affect any array expression in the AST, regardless of element type or array length. Single-element arrays would be particularly problematic as they would generate as empty arrays `[]`.

---
Repository: /testbed
