# Bug Report

### Describe the bug

Array expressions are being generated incorrectly when converting AST nodes to code. The first element of arrays is being skipped during code generation, resulting in arrays that are missing their initial element.

### Reproduction

When processing JavaScript code that contains array expressions, the generated output is missing the first array element:

```js
// Input code with array
const items = [1, 2, 3, 4];

// Generated output (incorrect)
const items = [2, 3, 4];
```

This affects any code generation that involves arrays, including:
- Simple array literals
- Arrays with mixed types
- Arrays in object properties
- Nested arrays

### Expected behavior

The code generator should preserve all array elements in their original order. For an input array `[1, 2, 3, 4]`, the output should be `[1, 2, 3, 4]`, not `[2, 3, 4]`.

### Additional context

This appears to be affecting MDX code generation. When MDX files contain arrays in their JavaScript expressions, the transpiled output has incorrect array values.

---
Repository: /testbed
