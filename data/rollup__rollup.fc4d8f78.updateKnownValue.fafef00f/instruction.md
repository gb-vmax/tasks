# Bug Report

### Describe the bug

I'm experiencing an issue with parameter variable optimization where function parameters are being incorrectly marked as reassigned even when they receive the same literal value across multiple calls. This seems to be causing unnecessary deoptimization.

### Reproduction

```js
function processValue(value) {
  return value * 2;
}

// Calling with the same literal value multiple times
processValue(5);
processValue(5);
processValue(5);
```

In this scenario, the parameter `value` should be recognized as having a consistent literal value (5) across calls, but instead it appears to be getting marked as reassigned incorrectly. This affects tree-shaking and optimization.

### Expected behavior

When a function parameter receives the same literal value across multiple invocations, it should maintain its known value status and not be marked as reassigned. The bundler should be able to optimize based on this consistent literal value.

### Additional context

This seems to have started happening recently. The logic for comparing literal values between arguments appears to be inverted - it's marking parameters as reassigned when the values match instead of when they differ.

---
Repository: /testbed
