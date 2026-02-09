# Bug Report

### Describe the bug

I'm experiencing an issue with do-while loops where side effects in the loop body are not being properly detected. It seems like the bundler is incorrectly tree-shaking code inside do-while statements even when the body should be executed.

### Reproduction

```js
let count = 0;

do {
  console.log('This should execute');
  count++;
} while (false);

console.log(count); // Expected: 1, but the loop body gets removed
```

The do-while loop body is being removed during bundling even though it should always execute at least once. This is causing my application to break because important side effects are being eliminated.

### Expected behavior

The do-while loop body should always be included in the bundle since it executes at least once regardless of the test condition. The bundler should recognize that the body has effects and preserve it.

### Additional context

This appears to be related to side effect detection in do-while statements. The issue doesn't occur with regular while loops, only do-while loops where the body is guaranteed to execute before the condition is checked.

---
Repository: /testbed
