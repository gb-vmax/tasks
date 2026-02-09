# Bug Report

### Describe the bug

I'm experiencing an issue with the AST visitor utility where it seems to be checking beyond the bounds of the test array. When using multiple test functions with the visitor, I'm getting unexpected behavior - it appears to be attempting to access one element past the end of the checks array.

### Reproduction

```js
const tests = [
  (node) => node.type === 'heading',
  (node) => node.type === 'paragraph'
];

// Create visitor with multiple test functions
visit(tree, tests, (node) => {
  console.log(node.type);
});
```

When the visitor tries to evaluate the test functions, it seems to iterate one position too far in the checks array, which could lead to calling `undefined` as a function or other unexpected behavior.

### Expected behavior

The visitor should only check against the actual test functions provided in the array, not attempt to access elements beyond the array length.

### Additional context

This seems to have started happening recently. The loop condition appears to be off-by-one, allowing iteration past the valid array indices.

---
Repository: /testbed
