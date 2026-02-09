# Bug Report

### Describe the bug

I'm experiencing an issue with `yield` expressions in my code. It seems like yield statements are being incorrectly removed or treated during tree-shaking, even when they should be preserved.

### Reproduction

```js
function* myGenerator() {
  yield someValue;
  // Other code that should be kept
}
```

When bundling code that contains generator functions with yield expressions, the bundler appears to be treating them incorrectly. The yield expressions seem to be getting removed when they shouldn't be, or vice versa - they're being kept when the context suggests they should be optimized away.

### Expected behavior

Yield expressions should be properly handled based on the execution context. When yields are supposed to be ignored for side-effect analysis, they should behave consistently with the rest of the bundler's tree-shaking logic.

### Additional context

This might be related to how the bundler analyzes side effects in generator functions. The issue appears to affect the final bundle output in unexpected ways.

---
Repository: /testbed
