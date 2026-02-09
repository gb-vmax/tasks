# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in for-of loops. Variables declared in the loop are not being properly tracked, leading to incorrect code elimination. It seems like the optimization is too aggressive and is removing code that should be preserved.

### Reproduction

```js
// Input code
const items = [1, 2, 3];
for (const item of items) {
  const result = item * 2;
  console.log(result);
}
```

When bundling this code, variables inside the for-of loop body are not being handled correctly during the tree-shaking phase. The deoptimization seems to be applied in the wrong direction - the loop variable itself should be deoptimized differently than the iterable.

### Expected behavior

The bundler should correctly preserve all necessary code within for-of loops and properly track dependencies between the loop variable and the iterable expression.

### Additional context

This appears to affect how the AST nodes are being analyzed during the tree-shaking pass. The issue is specifically with how paths are being deoptimized for the left-hand side (loop variable) versus the right-hand side (iterable expression).

---
Repository: /testbed
