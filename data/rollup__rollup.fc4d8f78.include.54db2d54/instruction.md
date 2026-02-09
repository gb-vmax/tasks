# Bug Report

### Describe the bug

When using try-catch-finally statements with tree-shaking enabled, the `brokenFlow` context is not being properly restored after processing the catch handler. This causes incorrect control flow analysis in subsequent code, potentially leading to incorrect tree-shaking behavior where code that should be included gets removed or vice versa.

### Reproduction

```js
// Input code
function test() {
  try {
    mayThrow();
    return 1;
  } catch (e) {
    console.log(e);
    return 2;
  } finally {
    cleanup();
  }
  // This code should be recognized as unreachable
  console.log('after try-catch-finally');
}
```

The issue occurs when the bundler processes try-catch-finally blocks. The control flow state after the catch block is not being correctly maintained, which can affect how the bundler determines which code is reachable.

### Expected behavior

The `brokenFlow` context should be properly restored after processing each part of the try-catch-finally statement to ensure accurate control flow analysis. Code following a try-catch-finally where all branches return should be correctly identified as unreachable.

### System Info

- Rollup version: latest
- Tree-shaking: enabled
- tryCatchDeoptimization: enabled

---
Repository: /testbed
