# Bug Report

### Describe the bug

When using function calls inside try-catch blocks, the bundler is not correctly handling variable marking for called functions. Functions that should be marked as being called from a try statement are not getting marked properly, which can lead to incorrect tree-shaking behavior.

### Reproduction

```js
try {
  someFunction();
} catch (e) {
  // handle error
}
```

In this scenario, `someFunction` should be marked as being called from a try statement, but the marking logic appears to be inverted. This affects how the bundler determines which code can be safely removed during tree-shaking.

### Expected behavior

Functions called within try-catch blocks should be properly marked so that the bundler can make correct decisions about code inclusion and side effects. The current behavior seems to be doing the opposite of what's intended.

### Additional context

This issue likely affects any code that relies on try-catch blocks for error handling, particularly when those blocks contain function calls that might have side effects. The problem appears to be related to the inclusion logic for call expressions.

---
Repository: /testbed
