# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking when using logical expressions (AND/OR operators) in my code. It appears that when the right branch of a logical expression should be included based on side effects, it's not being properly included in the bundle.

### Reproduction

```js
// Example code that demonstrates the issue
const condition = true;

// This should include both branches when left has side effects
const result = (console.log('left side'), false) || rightSideFunction();

function rightSideFunction() {
  return 'right';
}
```

When bundling this code, the right side of the logical OR expression is being incorrectly excluded even though the left side has side effects that should trigger inclusion of both branches.

### Expected behavior

Both the left and right branches of the logical expression should be included in the bundle when the left side contains side effects, regardless of which branch is determined to be "used". The tree-shaking should properly analyze the dependencies and include all necessary code.

### Additional context

This seems to be related to how logical expressions evaluate which branch should be included during the tree-shaking phase. The issue manifests when there are side effects in the left branch that should prevent aggressive optimization of the right branch.

---
Repository: /testbed
