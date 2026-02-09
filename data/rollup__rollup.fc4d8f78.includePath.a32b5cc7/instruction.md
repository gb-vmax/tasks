# Bug Report

### Describe the bug

When using the `arguments` object in a function with multiple parameters, only the first argument seems to be skipped during deoptimization. The rest of the arguments are being deoptimized incorrectly, which is causing issues with tree-shaking and code optimization.

### Reproduction

```js
function myFunction(a, b, c) {
  // Access arguments object
  console.log(arguments[0]);
  console.log(arguments[1]);
  console.log(arguments[2]);
}

// When bundling with rollup, the deoptimization
// doesn't handle all arguments properly
myFunction(1, 2, 3);
```

### Expected behavior

All arguments should be properly deoptimized when the `arguments` object is accessed. The current behavior seems to skip the first argument and only process arguments starting from index 1, which leads to incorrect optimization decisions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
