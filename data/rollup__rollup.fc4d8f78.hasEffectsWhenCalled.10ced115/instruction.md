# Bug Report

### Describe the bug

I'm encountering unexpected behavior with certain global functions when bundling code. It seems like some pure functions are being treated as having side effects when they shouldn't be, or vice versa.

### Reproduction

```js
// Example code that might be affected
const arr = [1, 2, 3];
const result = someGlobalFunction(arr, [4, 5, 6]);

// The bundler seems to be making incorrect assumptions about
// whether this call has side effects
```

When bundling code that uses certain built-in functions with array arguments, the tree-shaking behavior appears incorrect. Functions that should be considered pure are being kept in the bundle, or functions that might have effects are being removed.

### Expected behavior

The bundler should correctly identify when global functions with array parameters have side effects. Specifically:
- Functions called with a single argument should be handled correctly
- Functions called with an array as the second argument should be analyzed properly
- The tree-shaking should preserve/remove code based on accurate side effect detection

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the bundler determines purity of function calls when arrays are involved as arguments.

---
Repository: /testbed
