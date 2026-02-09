# Bug Report

### Describe the bug

I'm encountering an issue with assignment expressions where the left and right sides appear to be rendered in the wrong order in the generated output. When I have an assignment like `a = b`, the output seems to have the operands swapped.

### Reproduction

```js
// Input code
let x = 5;
x = 10;

// Expected output
let x = 5;
x = 10;

// Actual output appears to be
let x = 5;
10 = x;  // operands are reversed
```

This also affects destructuring assignments:

```js
const { foo, bar } = obj;
// The assignment sides seem to be flipped in the output
```

### Expected behavior

Assignment expressions should maintain the correct order with the left-hand side (the target) on the left and the right-hand side (the value) on the right. The generated code should preserve the semantics of the original assignment.

### Additional context

This started happening recently and affects all types of assignments including simple variable assignments, property assignments, and destructuring patterns. The bundled output has invalid syntax because of the reversed operands.

---
Repository: /testbed
