# Bug Report

### Describe the bug

I'm experiencing an issue where `for` loops with side effects in their body are being incorrectly tree-shaken out of the bundle. The loop body contains important side effects (like function calls or state mutations) but the entire loop is being removed during the build process.

### Reproduction

```js
// This for loop is being removed even though it has side effects
for (let i = 0; i < 10; i++) {
  console.log(i);
  someFunction();
}

// Another example - loop with side effects in body
for (let x = 0; x < arr.length; x++) {
  globalState.counter++;
}
```

After bundling, these loops are completely missing from the output even though they perform important operations.

### Expected behavior

For loops with side effects in their body should be preserved in the bundle. The tree-shaking algorithm should detect that the loop body has side effects and keep the entire loop statement.

### Additional context

This seems to have started happening recently. The loops are being treated as if they have no side effects and are safe to remove, but that's not the case when the body contains effectful code.

---
Repository: /testbed
