# Bug Report

### Describe the bug

I'm experiencing an issue with array expression code generation where the first element of arrays is being skipped. When generating code from AST nodes, arrays are missing their first element in the output.

### Reproduction

```js
// Input AST for array: [1, 2, 3]
const arrayNode = {
  type: 'ArrayExpression',
  elements: [
    { type: 'Literal', value: 1 },
    { type: 'Literal', value: 2 },
    { type: 'Literal', value: 3 }
  ]
};

// Generate code from the AST
const output = generateCode(arrayNode);

// Expected: [1, 2, 3]
// Actual: [2, 3]
```

The first element is consistently missing from the generated output. This affects any array expression being processed.

### Expected behavior

All array elements should be included in the generated code output, starting from index 0.

### Additional context

This seems to have started recently. Arrays with a single element end up being completely empty `[]`, and multi-element arrays are missing their first value.

---
Repository: /testbed
