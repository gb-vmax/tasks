# Bug Report

### Describe the bug

I'm experiencing an issue with conditional expressions (ternary operators) where the branches are being rendered in the wrong order. When code gets bundled, the consequent and alternate branches of ternary expressions appear swapped in the output.

### Reproduction

```js
// Input code
const result = condition ? valueIfTrue : valueIfFalse;

// Expected output
const result = condition ? valueIfTrue : valueIfFalse;

// Actual output (branches are swapped)
const result = condition ? valueIfFalse : valueIfTrue;
```

This causes the bundled code to have incorrect logic - when the condition is true, it returns the false branch value and vice versa.

### Expected behavior

The ternary operator should maintain the correct order of consequent and alternate branches during bundling. The true branch should come first after the `?` and the false branch should come after the `:`.

### Additional context

This seems to affect all conditional expressions in the code. The logic gets inverted which breaks the application behavior after bundling.

---
Repository: /testbed
