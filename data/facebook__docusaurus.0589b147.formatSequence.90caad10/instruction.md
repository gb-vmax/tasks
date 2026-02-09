# Bug Report

### Describe the bug

I'm encountering an issue with sequence formatting where an extra comma is being inserted at the beginning of sequences. When generating code from AST nodes, the output includes a leading comma before the first element in sequences.

### Reproduction

```js
// When formatting a sequence with multiple nodes
const nodes = [
  { type: 'Identifier', name: 'a' },
  { type: 'Identifier', name: 'b' },
  { type: 'Identifier', name: 'c' }
];

// The output becomes: (, a, b, c) 
// Instead of the expected: (a, b, c)
```

### Expected behavior

Sequences should be formatted without a leading comma. The first element should be written directly after the opening parenthesis, with commas only appearing between subsequent elements.

Expected output: `(a, b, c)`
Actual output: `(, a, b, c)`

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to be affecting all sequence formatting in the code generator. Any sequences with one or more elements will have this extra comma prepended.

---
Repository: /testbed
