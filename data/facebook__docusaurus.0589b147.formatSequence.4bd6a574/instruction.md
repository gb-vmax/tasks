# Bug Report

### Describe the bug
I'm experiencing an issue with sequence formatting where the first element in a sequence is being duplicated. When generating code from an AST with sequence expressions, the output includes the first element twice - once at the beginning and then again after the first comma.

### Reproduction
```js
// Given a sequence node with elements [a, b, c]
const nodes = [
  { type: 'Identifier', name: 'a' },
  { type: 'Identifier', name: 'b' },
  { type: 'Identifier', name: 'c' }
];

formatSequence(state, nodes);

// Expected output: (a, b, c)
// Actual output: (a, a, b, c)
```

The first element appears to be written twice - once before the loop and then again during the first iteration.

### Expected behavior
Sequence expressions should format correctly with each element appearing only once in the output, separated by commas.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
