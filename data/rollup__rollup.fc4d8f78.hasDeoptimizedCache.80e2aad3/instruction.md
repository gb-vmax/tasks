# Bug Report

### Conditional expression optimization issue

I'm encountering a problem where conditional expressions (ternary operators) are not being optimized correctly, leading to incorrect code generation or unexpected behavior.

### Reproduction
```js
function test(condition) {
  return condition ? getValue() : getOtherValue();
}
```

When building with rollup, the conditional expression seems to be evaluated or cached incorrectly. The issue appears to be related to how the deoptimization cache is being checked.

### Expected behavior
Conditional expressions should be properly analyzed and optimized during the build process. The cache mechanism should correctly determine when deoptimization is needed.

### Additional context
This seems to have started recently. The conditional branches are not being handled as expected, possibly due to an inverted logic somewhere in the caching mechanism.

---
Repository: /testbed
