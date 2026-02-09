# Bug Report

### Describe the bug

When using unlabeled `continue` statements in loops, the code after the continue is not being properly tree-shaken. Dead code that should be removed from the bundle is still being included in the output.

### Reproduction

```js
function example() {
  for (let i = 0; i < 10; i++) {
    if (i === 5) {
      continue;
    }
    console.log('This should be tree-shaken when continue is hit');
  }
  
  console.log('After loop');
}
```

In the above code, when the `continue` statement is executed, the flow is broken and subsequent code in that iteration should be recognized as unreachable. However, the bundler is not properly detecting this broken flow for unlabeled continue statements.

### Expected behavior

The bundler should recognize that unlabeled `continue` statements break the control flow within a loop iteration, allowing proper tree-shaking of unreachable code that follows the continue statement. This works correctly for labeled continue statements but fails for unlabeled ones.

### Additional context

This appears to be a regression - labeled continue statements are handled correctly and properly mark the flow as broken, but unlabeled continue statements are missing this behavior.

---
Repository: /testbed
