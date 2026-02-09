# Bug Report

### Describe the bug
When generating code for array expressions, the first element is being skipped. Arrays with multiple elements only output elements starting from index 1, causing the generated code to be incorrect.

### Reproduction
```js
// Given an array expression with multiple elements
const arrayNode = {
  type: 'ArrayExpression',
  elements: [
    { type: 'Literal', value: 1 },
    { type: 'Literal', value: 2 },
    { type: 'Literal', value: 3 }
  ]
};

// After code generation, the output is:
// [2, 3]
// instead of the expected:
// [1, 2, 3]
```

The first element of the array is completely missing from the generated output.

### Expected behavior
All array elements should be included in the generated code output. An array `[1, 2, 3]` should generate the string `"[1, 2, 3]"`, not `"[2, 3]"`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
