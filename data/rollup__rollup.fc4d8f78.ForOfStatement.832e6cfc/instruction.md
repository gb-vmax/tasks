# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in for-of loops. It seems like variables declared in the loop are not being properly tracked for side effects, leading to incorrect code elimination. The bundler is removing code that should be kept because it has observable side effects.

### Reproduction

```js
const items = [1, 2, 3];
let result = 0;

for (const item of items) {
  result += item;
  console.log(item);
}

console.log(result);
```

After bundling, the loop body appears to be incorrectly optimized, and some statements that should execute are being removed or not properly included in the output.

### Expected behavior

The for-of loop should correctly preserve all side effects in the loop body. Variables assigned within the loop should be properly tracked and their dependencies should be included in the bundle.

### Additional context

This seems to affect how the left-hand side (loop variable) and right-hand side (iterable) are being analyzed during the tree-shaking phase. The issue appears when the bundler tries to determine which parts of the code have side effects.

---
Repository: /testbed
