# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where the `else` branch of an `if` statement is being incorrectly included in the bundle even when the condition is known to be `true` at compile time.

### Reproduction

```js
// input.js
const ALWAYS_TRUE = true;

if (ALWAYS_TRUE) {
  console.log('This should be included');
} else {
  console.log('This should be tree-shaken out');
}
```

When bundling this code, both the `if` and `else` branches are included in the output, even though the condition is statically known to be `true`. The `else` branch should be removed during tree-shaking since it can never be executed.

### Expected behavior

The bundler should recognize that when a condition is always `true`, the `else` branch (alternate) is unreachable and should be excluded from the final bundle. Only the consequent branch should be included in this case.

### Additional context

This seems to be a regression - the tree-shaking was working correctly before. The issue affects code size as dead code from `else` branches is being unnecessarily included in production bundles.

---
Repository: /testbed
