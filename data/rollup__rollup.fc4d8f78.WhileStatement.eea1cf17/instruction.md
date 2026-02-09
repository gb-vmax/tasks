# Bug Report

### Describe the bug

I'm encountering an issue where while loops with side effects in their test conditions are being incorrectly tree-shaken. The condition expression gets removed even though it contains important side effects that should be preserved.

### Reproduction

```js
let count = 0;

function increment() {
  count++;
  return count < 5;
}

while (increment()) {
  // loop body
}

console.log(count); // Expected: 5, but the increment() calls are being removed
```

The `increment()` function in the while test condition has side effects (modifying `count`), but it seems like these effects are not being detected properly during the tree-shaking phase. The bundler is removing or not executing the test condition as expected.

### Expected behavior

While loop test conditions should be evaluated for side effects, and any functions with side effects in the condition should be preserved in the output bundle. The condition should always be included and executed properly.

### Additional context

This appears to be a regression - the same code worked correctly in previous versions. The issue specifically affects while statements where the test expression contains effectful operations.

---
Repository: /testbed
